P.1. ASTHMA PATIENT OVERVIEW [program:: ASTHMA PROGRAM$$ scope:: EXISTS$$includejs:: touchScreenToolkit;asthma]

Q.1.7. Patient History and Exposures [pos::6$$id::complications$$multiple:: multiple$$tt_beforeUnLoad::loadCheckConditions()$$tt_pageStyleClass::NoKeyboard]
O.1.7.1. Chronic dry cough
O.1.7.2. Indoor cooking
O.1.7.3. Occupational Exposure
O.1.7.4. TB Contact
O.1.7.5. Smoking
O.1.7.6. Secondhand smoking

Q.1.7.1.1. Chronic dry cough duration [pos:: 7$$field_type::number$$id::chronic_dry_cough0$$parent::Patient History and Exposures:Chronic dry cough$$tt_pageStyleClass :: Numeric NumbersOnly]

Q.1.7.1.2. Chronic dry cough Age onset   [pos::8 $$field_type::number$$ id::chronic_dry_cough1$$parent::Patient History and Exposures:Chronic dry cough]

Q.1.7.2.1. Indoor cooking date [pos:: 8$$field_type::date$$id::indoor_cooking_date$$parent::Patient History and Exposures:TB Contact]

Q.1.7.4.1. TB Contact Date [pos::9$$field_type::date$$ id::tb_contact_date$$parent::Patient History and Exposures:Indoor cooking]

Q.1.7.5.1. Smoking Date [pos:: 10$$field_type::date$$ id:: smoking_date$$parent::Patient History and Exposures:Smoking]

Q.1.7.6.1. Secondhand smocking Date [pos:: 11$$field_type::date$$ id::secondhand_smoking_date$$parent::Patient History and Exposures:Secondhand smoking]

Q.1.7.3.1. Occupation [pos:: 12$$ id:: occupation$$optional::true$$id::occupational_exposure0$$parent::Patient History and Exposures:Occupational Exposure]

Q.1.7.3.2. Occupation Exposure Date[pos:: 13$$field_type::date$$id::occupational_exposure1$$parent::Patient History and Exposures:Occupational Exposure]


