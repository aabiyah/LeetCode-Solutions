# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix. Return the result table in any order. 

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions REGEXP '\\bDIAB1';

