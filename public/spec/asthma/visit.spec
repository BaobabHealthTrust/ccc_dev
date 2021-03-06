P.1. ASTHMA VISIT [program:: ASTHMA PROGRAM$$ scope:: EXISTS$$includejs:: touchScreenToolkit;asthma]

Q.1.1. Visit Date [pos::0$$field_type::date$$tt_onUnLoad::validateWithBirthDate()]

Q.1.2. Planned Visit? [pos::1$$tt_requirenextclick::false$$parent::Visit Date]
O.1.2.1. Yes
O.1.2.2. No


Q.1.3. Patient is currently having an attack[pos::2$$tt_requirenextclick::false$$parent::Visit Date]
O.1.3.1. Yes
O.1.3.2. No

Q.1.4. Any triggers [pos::3$$tt_requirenextclick::false$$parent::Visit Date]
O.1.4.1. Yes 
O.1.4.2. No

Q.1.5. Symptoms[pos::4$$ multiple:: multiple$$parent::Visit Date$$ tt_onLoad :: enlargeHeight()]
O.1.5.1. Coughing
O.1.5.2. Shortness of breath
O.1.5.3. Wheezing
O.1.5.4. Stridor
O.1.5.5. Prolonged expiration
O.1.5.6. Central carinatus
O.1.5.7. Finger clubbing
O.1.5.8. Chronic cough
O.1.5.9. Chest tightiness

Q.1.5.2.1. Chronic dry cough duration [pos:: 11$$field_type::number$$id::chronic_dry_cough0$$parent::Visit Date$$tt_pageStyleClass :: Numeric NumbersOnly$$ min:: 1$$ Max:: 18]

Q.1.5.2.2. Chronic dry cough Age onset   [pos::12$$field_type::number$$ id::chronic_dry_cough1$$parent::Visit Date $$tt_onUnLoad::validateinputyear()]

Q.1.6. Day sx [pos::13$$field_type::number$$parent::Visit Date$$tt_pageStyleClass :: Numeric NumbersOnlyWithDecimal$$condition::false]

Q.1.7. Night sx [pos::14$$field_type::number$$parent::Visit Date$$tt_pageStyleClass :: Numeric NumbersOnlyWithDecimal$$condition::false]


Q.1.8. Beta-agonist inhaler use: frequency [pos::15$$tt_pageStyleClass :: NoKeyboard$$tt_requirenextclick::false$$parent::Visit Date]
O.1.8.1. Daily
O.1.8.2. Weekly
O.1.8.3. Monthly
O.1.8.4. Yearly
O.1.8.5. None

Q.1.9. Steroid inhaler daily? [pos::16$$tt_requirenextclick::false$$parent::Visit Date]
O.1.9.1. Yes
O.1.9.2. No

Q.1.10. Smoke? [pos::17$$id::do_smoke$$tt_requirenextclick::false$$parent::Visit Date]
O.1.10.1. Yes
O.1.10.2. No

Q.1.10.1.1. Number of cigarettes per day? [pos::18$$field_type::number$$condition::__$('do_smoke').value=='Yes'$$parent::Smoke?:Yes$$tt_pageStyleClass :: Numeric NumbersOnly$$min::1max::20$$parent::Visit Date]

Q.1.11. Passive smoking? [pos::19$$tt_requirenextclick::false$$parent::Visit Date]
O.1.11.1. Yes
O.1.11.2. No

Q.1.12. Indoor cooking? [pos::20$$tt_requirenextclick::false$$parent::Visit Date]
O.1.12.1. Yes
O.1.12.2. No

Q.1.13. Exacerbation today? [pos::21$$tt_requirenextclick::false$$parent::Visit Date]
O.1.13.1. Yes
O.1.13.2. No

Q.1.14. Asthma severity [pos::22$$tt_requirenextclick::false$$parent::Visit Date$$tt_pageStyleClass::NoKeyboard]
O.1.14.1. Mild
O.1.14.2. Moderate
O.1.14.3. Severe
O.1.14.4. Life Threatening


Q.1.15. Treatment [pos::23$$id::visit_treament$$ multiple:: multiple$$ tt_pageStyleClass::NoKeyboard$$parent::Visit Date]
O.1.15.1. Inhaled B-agonist
O.1.15.2. Inhaled steroid
O.1.15.3. Oral steroid
O.1.15.4. Other
O.1.15.5. None

Q.1.16. Other Treatment Specify [pos::24$$condition::__$('visit_treament').value=='Other'$$parent::Visit Date]

Q.1.17. Comment [pos::25$$optional::true$$parent::Visit Date]

Q.1.18. Summary [pos :: 26 $$ id:: summary $$ tt_onLoad::loadSummary() $$ tt_pageStyleClass::NoControls $$ helpText::Asthma Visit Summary $$condition::true]
