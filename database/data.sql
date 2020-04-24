DROP TABLE IF EXISTS `assistive_robot`.`goals`;
DROP TABLE IF EXISTS `assistive_robot`.`jobs`;

create table `assistive_robot`.`jobs`
(
    job_id       int auto_increment
        primary key,
    status       varchar(45) null,
    created_date datetime    null,
    updated_date datetime    null
);

create table `assistive_robot`.`goals`
(
	goal_id int auto_increment
		primary key,
	job_id int null,
	position_x decimal(10,7) null,
	position_y decimal(10,7) null,
	position_z decimal(10,7) null,
	orientation_x decimal(10,7) null,
	orientation_y decimal(10,7) null,
	orientation_z decimal(10,7) null,
	orientation_w decimal(10,7) null,
	status varchar(45) null,
	constraint goals_jobs_job_id_fk
		foreign key (job_id) references jobs (job_id)
);
