-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dictionary
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dictionary
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dictionary` DEFAULT CHARACTER SET utf8mb4 ;
USE `dictionary` ;

-- -----------------------------------------------------
-- Table `dictionary`.`celery_taskmeta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dictionary`.`celery_taskmeta` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `task_id` VARCHAR(155) NULL DEFAULT NULL,
  `status` VARCHAR(50) NULL DEFAULT NULL,
  `result` BLOB NULL DEFAULT NULL,
  `date_done` DATETIME NULL DEFAULT NULL,
  `traceback` TEXT NULL DEFAULT NULL,
  `name` VARCHAR(155) NULL DEFAULT NULL,
  `args` BLOB NULL DEFAULT NULL,
  `kwargs` BLOB NULL DEFAULT NULL,
  `worker` VARCHAR(155) NULL DEFAULT NULL,
  `retries` INT(11) NULL DEFAULT NULL,
  `queue` VARCHAR(155) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `task_id` (`task_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 467
DEFAULT CHARACTER SET = utf8mb4;





-- -----------------------------------------------------
-- Table `dictionary`.`tabledictionary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dictionary`.`tabledictionary` (
  `idWord` INT(11) NOT NULL AUTO_INCREMENT,
  `Expression` VARCHAR(45) NOT NULL,
  `Definition` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idWord`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `dictionary`.`tablemonitor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dictionary`.`tablemonitor` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `task_id` VARCHAR(155) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `result` VARCHAR(45) NULL DEFAULT NULL,
  `date_done` DATETIME NOT NULL,
  `traceback` VARCHAR(150) NULL DEFAULT NULL,
  `worker` VARCHAR(45) NOT NULL,
  `queue` VARCHAR(45) NOT NULL,
  `routing_key` VARCHAR(45) NOT NULL,
  `typeMethod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 689
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
