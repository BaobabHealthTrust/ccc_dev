P.1. ASTHMA PATIENT OVERVIEW [program:: ASTHMA PROGRAM$$ scope:: EXISTS$$includejs:: touchScreenToolkit;asthma]
Q.1.1. Diagnosis [pos:: 0$$id:: diagnosis$$ multiple:: multiple$$tt_beforeUnLoad::loadCheckConditions()]
O.1.1.1. Asthma
O.1.1.2. COPD

Q.1.2. Asthma diagnosis date [pos:: 1$$field_type::date$$ id:: asthma_date$$condition::false]

Q.1.3. COPD diagnosis date [pos:: 2$$field_type::date$$ id:: copd_date$$condition::false]

Q.1.4. Family History of Asthma? [pos:: 3$$tt_requirenextclick::false]
O.1.4.1. Yes
O.1.4.2. No

Q.1.5. Family History of COPD? [pos:: 4$$tt_requirenextclick::false]
O.1.5.1. Yes
O.1.5.2. No

Q.1.6. Patient History and Exposures [pos::5$$id::complications$$multiple:: multiple$$tt_beforeUnLoad::loadCheckConditions()$$tt_pageStyleClass::NoKeyboard]
O.1.6.1. Chronic dry cough
O.1.6.2. Indoor cooking
O.1.6.3. Occupational Exposure
O.1.6.4. TB Contact
O.1.6.5. Smoking
O.1.6.6. Secondhand smoking

Q.1.7. Chronic dry cough duration [pos:: 6$$field_type::number$$id::chronic_dry_cough0$$parent::Patient History and Exposures:Chronic dry cough$$tt_pageStyleClass :: Numeric NumbersOnly]

Q.1.8. Chronic dry cough Age onset   [pos::7 $$field_type::number$$ id::chronic_dry_cough1$$parent::Patient History and Exposures:Chronic dry cough$$tt_pageStyleClass :: Numeric NumbersOnly]

Q.1.9. Indoor cooking date [pos:: 8$$field_type::date$$id::indoor_cooking_date$$parent::Patient History and Exposures:TB Contact]

Q.1.10. TB Contact Date [pos::9$$field_type::date$$ id::tb_contact_date$$parent::Patient History and Exposures:Indoor cooking]

Q.1.11. Smoking Date [pos:: 10$$field_type::date$$ id:: smoking_date$$parent::Patient History and Exposures:Smoking]

Q.1.12. Secondhand smocking Date [pos:: 11$$field_type::date$$ id::secondhand_smoking_date$$parent::Patient History and Exposures:Secondhand smoking]

Q.1.13. Occupation [pos:: 12$$ id:: occupation$$optional::true$$id::occupational_exposure0$$parent::Patient History and Exposures:Occupational Exposure]
O.1.13.1. Business
O.1.13.2. Craftsman
O.1.13.3. Driver
O.1.13.4. Domestic worker
O.1.13.5. Farmer
O.1.13.6. Healthcare worker
O.1.13.7. Housewife
O.1.13.8. Mechanic
O.1.13.9. Messenger
O.1.13.10. Office worker
O.1.13.11. Police
O.1.13.12. Preschool child
O.1.13.13. Prisoner
O.1.13.14. Salesperson
O.1.13.15. Security guard
O.1.13.16. Soldier
O.1.13.17. Student
O.1.13.18. Teacher
O.1.13.19. Other

Q.1.14. Occupation Exposure Date[pos:: 13$$field_type::date$$id::occupational_exposure1$$parent::Patient History and Exposures:Occupational Exposure]


