P.1. UPDATE OUTCOME [program:: EPILEPSY PROGRAM$$ scope:: TODAY$$ includejs:: touchScreenToolkit;epilepsy]

Q.1.1. Outcome [pos:: 0$$ concept:: OUTCOME]
O.1.1.1. Discharge
O.1.1.2. Default
O.1.1.3. Treatment stopped
O.1.1.4. Transfer out

Q.1.1.4.1. Refer to clinic [pos:: 1$$ ajaxURL:: /static_locations?search_string=$$ allowFreeText:: true$$parent::Outcome:Transfer out]

Q.1.2. Outcome Date [pos:: 2$$ field_type:: date$$parent::Outcome]

Q.1.3. Notes [pos:: 3$$parent::Outcome]