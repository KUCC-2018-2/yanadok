INSERT INTO `user`(`id`, `password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`nickname`,`university`,`due_date`)
  VALUES (2,'1234',NULL,0,'ro dan','dan','ro','d@gmail.com',0,1,'2019-01-01 23:59:59.000000','dandandan','고려대학교','2020-01-01'),(3,'pbkdf2_sha256$120000$QZ94i6uzwnWK$V7hMPiiPuKTDI9FHXvcQ8CWjXZ16JCGaNGqaklGSILo=','2019-01-31 18:26:01.700749',0,'qwerty','Jay','Kim','rainy_waltz@naver.com',0,1,'2019-01-23 10:04:35.919614','TTd','고려대학교',NULL),(4,'pbkdf2_sha256$120000$HJwoxKU6Tit2$xBWLRRVGTQt9qsIil2AiBXgDuZfZ0p1A+S2YMx2UUwc=','2019-01-31 21:16:56.476436',1,'dandan','','','dd@gmail.com',1,1,'2019-01-24 02:49:48.892496',NULL,'고려대학교',NULL),(5,'pbkdf2_sha256$120000$GrI34XSqbJsR$0scERp+/BOF8GDrEVxsqmNljTiJwfA3DPQr6pSNVZvs=','2019-01-31 21:16:44.545443',1,'jack','','','',1,1,'2019-01-24 14:44:15.228578',NULL,'고려대학교',NULL);
INSERT INTO `course` VALUES (0,'JMCO203-01','2019-01','고려대학교',' 서울','전공필수','미디어학입문','최현철',3),(1,'JMCO267-00','2019-01','고려대학교',' 서울','전공필수','광고의이해','최세정',3),(2,'JMCO447-00','2019-01','고려대학교',' 서울','전공필수','PR캠페인','윤영민',3),(3,'KORE107-00','2019-01','고려대학교',' 서울','교양','한국고전의세계','안득용',3);
INSERT INTO `post` VALUES (33,'test1',NULL,'tatata','공지사항',NULL,'2019-01-24 23:11:21.541299',0,5),(34,'qwdf',NULL,'fdqqqqqq','공지사항',NULL,'2019-01-24 23:45:03.747399',0,3),(35,'test db',NULL,'ddddd','공지사항',NULL,'2019-01-24 23:49:54.904595',0,3);
INSERT INTO `comment` VALUES (6,'asd','2019-01-31 20:26:13.508176',35,4),(7,'ss','2019-01-31 20:26:13.508176',35,4),(8,'hi','2019-01-31 20:26:13.508176',35,4),(9,'hi2','2019-01-31 20:26:13.508176',35,4);


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'MON');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'MON');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'TUE');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'TUE');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'WED');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'WED');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'THU');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'THU');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'FRI');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'FRI');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'SAT');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'SAT');


INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (1, '2019-01-01 09:00:00.000000', '2019-01-01 10:30:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (2, '2019-01-01 10:30:00.000000', '2019-01-01 12:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (3, '2019-01-01 12:00:00.000000', '2019-01-01 13:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (4, '2019-01-01 13:00:00.000000', '2019-01-01 14:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (5, '2019-01-01 14:00:00.000000', '2019-01-01 15:30:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (6, '2019-01-01 15:30:00.000000', '2019-01-01 17:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (7, '2019-01-01 17:00:00.000000', '2019-01-01 18:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (8, '2019-01-01 18:00:00.000000', '2019-01-01 19:00:00.000000', 'SUN');
INSERT INTO `course_time`(`order`, `start_time`, `end_time`, `course_day`) VALUES (9, '2019-01-01 19:00:00.000000', '2019-01-01 20:00:00.000000', 'SUN');

INSERT INTO `course_space_time`(`id`,`course_id`,`course_time_id`,`classroom`) VALUES (1, 0, 2, '미디어관 412호'),
                                         (2, 0, 20, '미디어관 412호'),
                                         (3, 1, 14, '미디어관 602호'),
                                         (4, 1, 32, '미디어관 602호'),
                                        (5, 2, 14, '미디어관 412호'),
                                        (6, 2, 32, '미디어관 412호'),
                                        (7, 3, 3, '법학관신관 206호'),
                                        (8, 3, 21,'법학관신관 206호'),
                                        (9, 3, 4, '법학관신관 206호'),
                                        (10, 3, 22, '법학관신관 206호');