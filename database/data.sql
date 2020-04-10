DROP TABLE IF EXISTS `assistive_robot`.jobs;
DROP TABLE IF EXISTS `assistive_robot`.goals;

create table jobs
(
    job_id       int auto_increment
        primary key,
    status       varchar(45) null,
    created_date datetime    null,
    updated_date datetime    null
);

create table goals
(
    goal_id       int auto_increment
        primary key,
    job_id        int            not null,
    position_x    decimal(10, 7) not null,
    position_y    decimal(10, 7) not null,
    position_z    decimal(10, 7) not null,
    orientation_x decimal(10, 7) not null,
    orientation_y decimal(10, 7) not null,
    orientation_z decimal(10, 7) not null,
    orientation_w decimal(10, 7) not null
);

INSERT INTO `assistive_robot`.jobs (job_id, status, created_date, updated_date)
VALUES (1, 'pending', '2020-04-05 00:00:00', null),
       (2, 'pending', '2020-04-05 00:00:00', null);

INSERT INTO `assistive_robot`.goals (goal_id, job_id, position_x, position_y, position_z, orientation_x, orientation_y,
                                     orientation_z, orientation_w)
VALUES (1, 1, '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345'),
       (2, 1, '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345'),
       (3, 2, '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345'),
       (4, 2, '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345', '1.2345');