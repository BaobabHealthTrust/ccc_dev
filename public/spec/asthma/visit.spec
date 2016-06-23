P.1.  ASTHMA VISIT [program:: ASTHMA PROGRAM$$ scope:: TODAY$$ includejs:: touchScreenToolkit;epilepsy]
Q.1.1. Visit Date [pos::0$$field_type::date]

Q.1.2. Planned Visit? [pos::1$$tt_requirenextclick::false]
O.1.2.1. Yes
O.1.2.2. No

Q.1.3. Weight (Kg) [pos::2$$field_type::number]

Q.1.4. Day sx [pos::3$$field_type::number]

Q.1.5. Night sx [pos::4$$field_type::number]


Q.1.6. Beta-agonist inhaler use: frequency [pos::5$$tt_requirenextclick::false]
O.1.6.1. day
O.1.6.2. wk
O.1.6.3. mo
O.1.6.4. yr

Q.1.7. Steroid inhaler daily? [pos::6$$tt_requirenextclick::false]
O.1.7.1. Yes
O.1.7.2. No

Q.1.8. Smoke? [pos::7$$id::do_smoke$$tt_requirenextclick::false]
O.1.8.1. Yes
O.1.8.2. No

Q.1.9. Number of cigarette per day? [pos::8$$field_type::number$$condition::__$('do_smoke').value=='Yes']

Q.1.10. Passive smoking? [pos::9$$tt_requirenextclick::false]
O.1.10.1. Yes
O.1.10.2. No

Q.1.11. Indoor cooking? [pos::10$$tt_requirenextclick::false]
O.1.11.1. Yes
O.1.11.2. No

Q.1.12. Exacerbation today? [pos::11$$tt_requirenextclick::false]
O.1.12.1. Yes
O.1.12.2. No

Q.1.13. Asthma severity [pos::12$$tt_requirenextclick::false]
O.1.13.1. Not Asthma
O.1.13.2. Intemittent
O.1.13.3. Mild persistent
O.1.13.4. Mod persistent
O.1.13.5. Severe persistent
O.1.13.2. Uncontrolled


Q.1.14. Treatment [pos::13$$id::visit_treament$$tt_requirenextclick::false]
O.1.14.1. Inhaled B-agonist
O.1.14.2. Inhaled steroid
O.1.14.3. Oral steroid
O.1.14.4. Other

Q.1.15. Other Treatment Specify [pos::14$$condition::__$('visit_treament').value=='Other']

Q.1.16. Comment [pos::15$$optional::true]

Q.1.17. Next appointment Date [pos::16$$field_type::date]

