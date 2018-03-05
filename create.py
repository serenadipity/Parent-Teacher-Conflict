import database_utils
database_utils.valid_create_parent('TriciaCardinal', 'ABCabc1!', 'ABCabc1!', 'Tricia', 'Cardinal', 'TriciaCardinal@gmail.com')
database_utils.valid_create_parent('AlfredGarvey', 'ABCabc1!', 'ABCabc1!', 'Alfred', 'Garvey', 'AlfredGarvey@gmail.com')
database_utils.valid_create_parent('JustaJakes', 'ABCabc1!', 'ABCabc1!', 'Justa', 'Jakes', 'JustaJakes@gmail.com')
database_utils.valid_create_parent('SamDewar', 'ABCabc1!', 'ABCabc1!', 'Sam', 'Dewar', 'SamDewar@gmail.com')
database_utils.valid_create_parent('MelinaKnaub', 'ABCabc1!', 'ABCabc1!', 'Melina', 'Knaub', 'MelinaKnaub@gmail.com')
database_utils.valid_create_parent('JanaStapp', 'ABCabc1!', 'ABCabc1!', 'Jana', 'Stapp', 'JanaStapp@gmail.com')
database_utils.valid_create_parent('GemmaBellantoni', 'ABCabc1!', 'ABCabc1!', 'Gemma', 'Bellantoni', 'GemmaBellantoni@gmail.com')
database_utils.valid_create_parent('OctaviaChirico', 'ABCabc1!', 'ABCabc1!', 'Octavia', 'Chirico', 'OctaviaChirico@gmail.com')
database_utils.valid_create_parent('XavierHammes', 'ABCabc1!', 'ABCabc1!', 'Xavier', 'Hammes', 'XavierHammes@gmail.com')
database_utils.valid_create_parent('SocorroBosworth', 'ABCabc1!', 'ABCabc1!', 'Socorro', 'Bosworth', 'SocorroBosworth@gmail.com')
database_utils.valid_create_parent('PorshaConey', 'ABCabc1!', 'ABCabc1!', 'Porsha', 'Coney', 'PorshaConey@gmail.com')
database_utils.valid_create_parent('HazelBonn', 'ABCabc1!', 'ABCabc1!', 'Hazel', 'Bonn', 'HazelBonn@gmail.com')
database_utils.valid_create_parent('JacquilineHesler', 'ABCabc1!', 'ABCabc1!', 'Jacquiline', 'Hesler', 'JacquilineHesler@gmail.com')
database_utils.valid_create_parent('KarlMccardell', 'ABCabc1!', 'ABCabc1!', 'Karl', 'Mccardell', 'KarlMccardell@gmail.com')
database_utils.valid_create_parent('DonaldMccardall', 'ABCabc1!', 'ABCabc1!', 'Donald', 'Mccardall', 'DonaldMccardall@gmail.com')
database_utils.valid_create_parent('MirnaPenner', 'ABCabc1!', 'ABCabc1!', 'Mirna', 'Penner', 'MirnaPenner@gmail.com')
database_utils.valid_create_parent('MaribelHughey', 'ABCabc1!', 'ABCabc1!', 'Maribel', 'Hughey', 'MaribelHughey@gmail.com')
database_utils.valid_create_parent('OneidaDrews', 'ABCabc1!', 'ABCabc1!', 'Oneida', 'Drews', 'OneidaDrews@gmail.com')
database_utils.valid_create_parent('KathieKorando', 'ABCabc1!', 'ABCabc1!', 'Kathie', 'Korando', 'KathieKorando@gmail.com')
database_utils.valid_create_parent('MoseEilerman', 'ABCabc1!', 'ABCabc1!', 'Mose', 'Eilerman', 'MoseEilerman@gmail.com')
database_utils.valid_create_teacher('JCocoros', 'ABCabc1!', 'ABCabc1!', 'Jim', 'Cocoros', 'JCocoros@stuy.edu', 'Stuyvesant', '407')
database_utils.valid_create_teacher('AJaishankar', 'ABCabc1!', 'ABCabc1!', 'Ashvin', 'Jaishankar', 'AJaishankar@stuy.edu', 'Stuyvesant', '427')
database_utils.valid_create_teacher('MZamansky', 'ABCabc1!', 'ABCabc1!', 'Mike', 'Zamansky', 'MZamansky@stuy.edu', 'Stuyvesant', '307')
database_utils.valid_create_teacher('OPascu', 'ABCabc1!', 'ABCabc1!', 'Oana', 'Pascu', 'OPascu@stuy.edu', 'Stuyvesant', '431')

database_utils.set_teacher_availability(1, '2016-01-28', 'evening')
database_utils.make_appointment(1, 1, '2016-01-28', 'evening', 3)
database_utils.make_appointment(2, 1, '2016-01-28', 'evening', 6)
database_utils.make_appointment(3, 1, '2016-01-28', 'evening', 9)
database_utils.make_appointment(4, 1, '2016-01-28', 'evening', 12)
database_utils.make_appointment(5, 1, '2016-01-28', 'evening', 15)
database_utils.make_appointment(6, 1, '2016-01-28', 'evening', 18)
database_utils.make_appointment(7, 1, '2016-01-28', 'evening', 21)
database_utils.make_appointment(8, 1, '2016-01-28', 'evening', 24)
database_utils.make_appointment(9, 1, '2016-01-28', 'evening', 27)
database_utils.make_appointment(10, 1, '2016-01-28', 'evening', 30)
database_utils.make_appointment(11, 1, '2016-01-28', 'evening', 33)
database_utils.make_appointment(12, 1, '2016-01-28', 'evening', 36)
database_utils.make_appointment(13, 1, '2016-01-28', 'evening', 39)
database_utils.make_appointment(14, 1, '2016-01-28', 'evening', 42)
database_utils.make_appointment(15, 1, '2016-01-28', 'evening', 45)
database_utils.make_appointment(16, 1, '2016-01-28', 'evening', 48)
database_utils.make_appointment(17, 1, '2016-01-28', 'evening', 51)
database_utils.make_appointment(18, 1, '2016-01-28', 'evening', 54)
database_utils.make_appointment(19, 1, '2016-01-28', 'evening', 57)
database_utils.make_appointment(20, 1, '2016-01-28', 'evening', 60)