P.1. DIABETES HISTORY [program:: DIABETES PROGRAM$$ scope:: TODAY$$ includejs:: touchScreenToolkit;dm]

Q.1.1. Diabetes Diagnosis Date [pos:: 0$$ id:: initial_diagnosis_date$$ field_type:: birthdate$$ condition:: !existingDiabetesPatient()$$ estimate_label:: Number of years ago]

Q.1.2. Type of diabetes [pos:: 1]
O.1.2.1. Type 1 Diabetes
O.1.2.2. Type 2 Diabetes
O.1.2.3. Unknown

Q.1.3. Secondary diabetes? [pos:: 2$$ tt_requireNextClick :: false]
O.1.3.1. No
O.1.3.2. Yes

Q.1.3.2.1. Cause of Secondary Diabetes [pos:: 3$$ flag:: {"message":"Please update  HIV status screen", "condition":"ART"}$$ tt_requireNextClick:: false]
O.1.3.2.1.1. ART
O.1.3.2.1.2. Corticosteroids
O.1.3.2.1.3. Other

Q.1.3.2.1.3.1. Specify Other Cause of Diabetes [pos:: 4]

Q.1.4. Family History (blood relatives only) [pos:: 5]
O.1.4.1. Positive
O.1.4.2. Negative
O.1.4.3. Unknown

