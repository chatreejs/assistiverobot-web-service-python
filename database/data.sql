DROP TABLE IF EXISTS `assistive_robot`.jobs;
DROP TABLE IF EXISTS `assistive_robot`.goals;

create table jobs
(
    job_id       int auto_increment
        primary key,
    status       varchar(45) null,
    created_date date        null,
    updated_date datetime    null
);

create table goals
(
    goal_id       int auto_increment
        primary key,
    jobs_id       int             not null,
    position_x    decimal(20, 10) not null,
    position_y    decimal(20, 10) not null,
    position_z    decimal(20, 10) null,
    orientation_x decimal(20, 10) not null,
    orientation_y decimal(20, 10) not null,
    orientation_z decimal(20, 10) not null,
    orientation_w decimal(20, 10) not null
);

INSERT INTO `assistive_robot`.jobs (job_id, status, created_date, updated_date)
VALUES (1, 'pending', '2020-04-05 00:00:00', null),
       (2, 'pending', '2020-04-05 00:00:00', null);

INSERT INTO `assistive_robot`.goals (goal_id, jobs_id, position_x, position_y, position_z, orientation_x, orientation_y,
                                     orientation_z, orientation_w)
VALUES (1, 1, '0', '0', '0', '0', '0', '0', '0'),
       (2, 1, '0', '0', '0', '0', '0', '0', '0');