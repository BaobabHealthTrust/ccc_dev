P.1. UPDATE OUTCOME [program:: HYPERTENSION PROGRAM$$ scope:: TODAY$$ includejs:: touchScreenToolkit;htn]

Q.1.1. Outcome [pos:: 0$$ concept:: OUTCOME$$tt_requirenextclick::false$$tt_pageStyleClass :: NoKeyboard]
O.1.1.1. Admitted
O.1.1.2. Home
O.1.1.3. Treatment changed
O.1.1.4. Treatment stopped
O.1.1.5. Transfer out
O.1.1.6. Dead

Q.1.1.5.1. Refer to clinic [pos:: 1$$ ajaxURL:: /facilities?name=$$ allowFreeText:: true]

Q.1.2. Outcome Date [pos:: 2$$ field_type:: date $$ parent :: OUTCOME validateWithBirthDate()]

Q.1.3. Notes [pos:: 3 $$ optional:: true $$ parent :: OUTCOME]

Q.1.4. Summary [pos :: 4 $$ id:: summary $$ tt_onLoad::loadSummary() $$ tt_pageStyleClass::NoControls $$ helpText::Outcome Summary $$condition::true]