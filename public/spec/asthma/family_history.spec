P.1. ASTHMA FAMILY HISTORY [program:: ASTHMA PROGRAM$$ scope:: EXISTS$$includejs:: touchScreenToolkit;asthma]

Q.1.1. Family History of Asthma? [pos:: 0$$tt_requirenextclick::false]
O.1.1.1. Yes
O.1.1.2. No
O.1.1.3. Unknown

Q.1.2. Family History of COPD? [pos:: 1$$tt_requirenextclick::false$$parent::Family History of Asthma? ]
O.1.2.1. Yes
O.1.2.2. No
O.1.2.3. Unknown

Q.1.3. Family History of TB? [pos:: 2$$parent::Family History of Asthma?]
O.1.3.1. Yes
O.1.3.2. No
O.1.3.3. Unknown

Q.1.4. Summary [pos :: 3 $$ id:: summary $$ tt_onLoad::loadSummary() $$ tt_pageStyleClass::NoControls $$ helpText::Asmatha Family History Summary $$condition::true]
