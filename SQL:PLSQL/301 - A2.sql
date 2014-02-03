/*
  Assignment 2
  
  Student Name: Thanusha Thaninayagam

  'This Assignment represents my work in accordance 
                  with the Seneca Academic Policy.'
  Signature: Thanusha Thaninayagam
*/

CREATE OR REPLACE 
PACKAGE ClassPackage AS 

  /* TODO enter package declarations (types, exceptions, methods etc) here */ 
  TYPE t_StudentIDTable IS TABLE OF Registered_Students.student_id%TYPE
        INDEX BY BINARY_INTEGER;
  e_StudentNotRegistered EXCEPTION;
  
  -- Procedures
  PROCEDURE AddRegisteredStudent (p_StudentID IN students.ID%TYPE,
                                  p_Department IN classes.department%TYPE,
                                  p_Course IN classes.course%TYPE);
  PROCEDURE RemoveRegisteredStudent (p_StudentID IN students.ID%TYPE,
                                     p_Department IN classes.department%TYPE,
                                     p_Course IN classes.course%TYPE);
  PROCEDURE UpdateGrade (p_Department IN registered_students.department%TYPE,
                         p_Course IN registered_Students.course%TYPE);
  PROCEDURE ClassList (p_Department IN classes.department%TYPE,
                       p_Course IN classes.course%TYPE,
                       p_IDs OUT t_StudentIDTable,
                       p_NumStudents IN OUT BINARY_INTEGER);
                       
  PROCEDURE UpdateStudent (p_StudentID IN students.ID%TYPE,
                           p_Major IN students.major%TYPE);
  PROCEDURE DeleteStudent (p_StudentID IN students.ID%TYPE);
  PROCEDURE InsertStudent (p_StudentID IN students.ID%TYPE,
                           p_FirstName IN students.first_name%TYPE,
                           p_LastName students.last_name%TYPE);
  
  -- Functions                         
  FUNCTION FullName (p_StudentID IN students.ID%TYPE)
    RETURN VARCHAR2;
  FUNCTION CountCredits (p_StudentID IN students.ID%TYPE)
    RETURN NUMBER;

END ClassPackage;


CREATE OR REPLACE PACKAGE BODY ClassPackage IS


  -- AddRegisteredStudent
  PROCEDURE AddRegisteredStudent (
    p_StudentID  IN students.id%TYPE,
    p_Department IN classes.department%TYPE,
    p_Course      IN classes.course%TYPE)
  IS
  BEGIN
    -- Insert student into Registered_Students
    INSERT INTO registered_students(student_id, department, course, grade)
        VALUES (p_StudentID, p_Department, p_Course, NULL);
    COMMIT;
  END AddRegisteredStudent;
 

  -- RemoveRegisteredSstudent
  PROCEDURE RemoveRegisteredStudent (
    p_StudentID   IN students.ID%TYPE,
    p_Department  IN classes.department%TYPE,
    p_Course      IN classes.course%TYPE)
  IS
  BEGIN
    -- Deleting student from Registered_Students
    DELETE FROM Registered_Students
    WHERE student_id = p_StudentID
    AND department = p_Department
    AND course = p_Course;
    
    IF SQL%NOTFOUND THEN
      RAISE e_StudentNotRegistered;
    END IF;
    COMMIT;
    
    EXCEPTION
      WHEN e_StudentNotRegistered THEN
        DBMS_OUTPUT.PUT_LINE('Student is not registered');
  END RemoveRegisteredStudent; 
  
  
  -- UpdateGrade
  PROCEDURE UpdateGrade (
    p_Department  IN registered_students.department%TYPE,
    p_Course      IN registered_Students.course%TYPE)
  IS
    CURSOR his301_cur IS SELECT * FROM HIS301;
    v_Letter VARCHAR2(1);
  BEGIN 
  
    FOR student IN his301_cur LOOP
      
      -- For each student in his301_cur, 
      -- get a char grade (v_Letter) instead of a number grade
      IF student.grade = 1 THEN v_Letter := 'A';
      ELSIF student.grade = 2 THEN v_Letter := 'B';
      ELSIF student.grade = 3 THEN v_Letter := 'C';
      ELSIF student.grade = 4 THEN v_Letter := 'D';
      ELSIF student.grade = 5 THEN v_Letter := 'E';
      END IF;                                   
      
      -- Then update Registered_Students grade column
      UPDATE registered_students
      SET grade = TO_CHAR(v_Letter)
      WHERE student_id = student.student_id 
      AND department = p_Department 
      AND course = p_Course;
      
      IF SQL%NOTFOUND THEN
        RAISE e_StudentNotRegistered;
      END IF;
      COMMIT;

    END LOOP;
        
    EXCEPTION 
      WHEN e_StudentNotRegistered THEN
        DBMS_OUTPUT.PUT_LINE('Student is not registered');
  END UpdateGrade;
  
  
  -- ClassList
  PROCEDURE ClassList (
    p_Department  IN classes.department%TYPE,
    p_Course      IN classes.course%TYPE,
    p_IDs         OUT t_StudentIDTable,
    p_NumStudents IN OUT BINARY_INTEGER)
  IS
    v_Counter NUMBER := 0;
    CURSOR sid_cur IS 
      SELECT student_id FROM registered_students 
      WHERE department = p_Department AND course = p_Course;
  BEGIN
    
    -- Total number of students in the class
    SELECT COUNT(*)
    INTO p_NumStudents
    FROM Registered_Students
    WHERE department = p_Department
    AND course = p_Course;
    
    FOR s_id IN sid_cur LOOP
    
      -- For every student in sid_cur,
      -- put into p_IDs table
      p_IDs(v_Counter) := s_id.student_id;
      v_Counter := v_Counter + 1;
    
    END LOOP;
    
  END ClassList;
  

  -- Maintaining the Students Table
  -- UpdateStudent  
  PROCEDURE UpdateStudent (
    p_StudentID IN students.ID%TYPE,
    p_Major     IN students.major%TYPE)
  IS
  BEGIN
    -- Updating the Students major column
    UPDATE students
    SET major = p_Major
    WHERE ID = p_StudentID;
    COMMIT;
  END UpdateStudent;

  
  -- DeleteStudent
  PROCEDURE DeleteStudent (
    p_StudentID IN students.id%TYPE)
  IS
  BEGIN
    -- Delete student from the Students table
    DELETE FROM students
    WHERE ID = p_StudentID;
    COMMIT;
  END DeleteStudent;
  

  -- InsertStudent
  PROCEDURE InsertStudent (
    p_StudentID IN students.ID%TYPE,
    p_FirstName IN students.first_name%TYPE,
    p_LastName  IN students.last_name%TYPE)
  IS
  BEGIN
    -- Insert student into the Students table
    INSERT INTO students(ID, first_name, last_name)
      VALUES (p_StudentID, p_FirstName, p_LastName);
    COMMIT;
  END InsertStudent;
  
  
  -- Functions
  -- FullName
  FUNCTION FullName (
    p_StudentID IN students.id%TYPE)
    RETURN VARCHAR2 
  IS
    v_FullName  VARCHAR2(40);
  BEGIN
      -- Return the full name of the p_StudentID
      SELECT first_name ||' '|| last_name
      INTO v_FullName
      FROM students
      WHERE ID = p_StudentID;
      RETURN v_FullName;
  END FullName;
  
  
  -- CountCredits
  FUNCTION CountCredits (
    p_StudentID IN students.ID%TYPE)
    RETURN NUMBER 
  IS
    CURSOR sid_cur IS 
      SELECT * FROM Registered_Students WHERE student_id = p_StudentID;
    v_CountC NUMBER := 0;
  BEGIN
  
    FOR course IN sid_cur LOOP
      
      -- For each course grade, add the credit value into v_CountC
      IF course.grade = 'A' THEN v_CountC := v_CountC + 5;
      ELSIF course.grade = 'B' THEN v_CountC := v_CountC + 4;
      ELSIF course.grade = 'C' THEN v_CountC := v_CountC + 3;
      ELSIF course.grade = 'D' THEN v_CountC := v_CountC + 2;
      ELSIF course.grade = 'E' THEN v_CountC := v_CountC + 1;
      END IF;
      
    END LOOP;
    
    IF SQL%NOTFOUND THEN
      RAISE e_StudentNotRegistered;
    END IF;
    
    EXCEPTION
      WHEN e_StudentNotRegistered THEN
        DBMS_OUTPUT.PUT_LINE('Student is not registered 
                              and does not have any credits.');
    
    RETURN v_CountC;
  END CountCredits;
  
END ClassPackage;