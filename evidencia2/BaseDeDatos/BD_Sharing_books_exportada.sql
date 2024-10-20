-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema sharing_books
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sharing_books
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sharing_books` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `sharing_books` ;

-- -----------------------------------------------------
-- Table `sharing_books`.`domicilio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`domicilio` (
  `ID_domicilio` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(70) NOT NULL,
  `altura` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(70) NOT NULL,
  `pais` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_domicilio`),
  UNIQUE INDEX `ID_domicilio_UNIQUE` (`ID_domicilio` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharing_books`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`usuario` (
  `ID_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(60) NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_nacimiento` DATE NULL DEFAULT NULL,
  `telefono` VARCHAR(45) NULL DEFAULT NULL,
  `e_mail` VARCHAR(70) NOT NULL,
  `password` VARCHAR(70) NOT NULL,
  `ID_domicilio` INT NULL DEFAULT NULL,
  `deleted_at` DATE NULL DEFAULT NULL,
  `usuariocol` VARCHAR(45) NULL DEFAULT NULL,
  `DNI` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE INDEX `ID_usuario_UNIQUE` (`ID_usuario` ASC) VISIBLE,
  UNIQUE INDEX `nombre_usuario_UNIQUE` (`nombre_usuario` ASC) VISIBLE,
  UNIQUE INDEX `DNI_UNIQUE` (`DNI` ASC) VISIBLE,
  INDEX `ID_domicilio_idx` (`ID_domicilio` ASC) VISIBLE,
  CONSTRAINT `ID_domicilio`
    FOREIGN KEY (`ID_domicilio`)
    REFERENCES `sharing_books`.`domicilio` (`ID_domicilio`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharing_books`.`acceso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`acceso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuarioLogueado` INT NULL DEFAULT NULL,
  `fechaIngreso` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaSalida` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `usuarioLogueado` (`usuarioLogueado` ASC) VISIBLE,
  CONSTRAINT `acceso_ibfk_1`
    FOREIGN KEY (`usuarioLogueado`)
    REFERENCES `sharing_books`.`usuario` (`ID_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharing_books`.`libro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`libro` (
  `ID_libro` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(100) NULL DEFAULT NULL,
  `autor` VARCHAR(70) NULL DEFAULT NULL,
  `editorial` VARCHAR(50) NULL DEFAULT NULL,
  `fecha_publicacion` DATE NULL DEFAULT NULL,
  `genero` VARCHAR(45) NULL DEFAULT NULL,
  `ID_usuario` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID_libro`),
  UNIQUE INDEX `ID_libro_UNIQUE` (`ID_libro` ASC) VISIBLE,
  INDEX `ID_usuario_idx` (`ID_usuario` ASC) VISIBLE,
  CONSTRAINT `ID_usuario`
    FOREIGN KEY (`ID_usuario`)
    REFERENCES `sharing_books`.`usuario` (`ID_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharing_books`.`punto_encuentro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`punto_encuentro` (
  `ID_punto_encuentro` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `ID_domicilio` INT NULL DEFAULT NULL,
  `descripcion` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_punto_encuentro`),
  UNIQUE INDEX `ID_punto_encuentro_UNIQUE` (`ID_punto_encuentro` ASC) VISIBLE,
  INDEX `ID_domicilio_idx` (`ID_domicilio` ASC) VISIBLE,
  CONSTRAINT `ID_domicilio_p_e`
    FOREIGN KEY (`ID_domicilio`)
    REFERENCES `sharing_books`.`domicilio` (`ID_domicilio`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharing_books`.`intercambio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`intercambio` (
  `ID_intercambio` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha_intercambio` DATE NULL DEFAULT NULL,
  `ID_usuario1` INT NULL DEFAULT NULL,
  `ID_libro1` INT NULL DEFAULT NULL,
  `ID_usuario2` INT NULL DEFAULT NULL,
  `ID_libro2` INT NULL DEFAULT NULL,
  `ID_punto_encuentro` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID_intercambio`),
  INDEX `ID_usuario1_idx` (`ID_usuario1` ASC) VISIBLE,
  INDEX `ID_usuario2_idx` (`ID_usuario2` ASC) VISIBLE,
  INDEX `ID_libro1_idx` (`ID_libro1` ASC) VISIBLE,
  INDEX `ID_libro2_idx` (`ID_libro2` ASC) VISIBLE,
  INDEX `ID_punto_encuentro_idx` (`ID_punto_encuentro` ASC) VISIBLE,
  CONSTRAINT `FK_libro1`
    FOREIGN KEY (`ID_libro1`)
    REFERENCES `sharing_books`.`libro` (`ID_libro`),
  CONSTRAINT `FK_libro2`
    FOREIGN KEY (`ID_libro2`)
    REFERENCES `sharing_books`.`libro` (`ID_libro`),
  CONSTRAINT `FK_punto_encuentro`
    FOREIGN KEY (`ID_punto_encuentro`)
    REFERENCES `sharing_books`.`punto_encuentro` (`ID_punto_encuentro`),
  CONSTRAINT `FK_usuario1`
    FOREIGN KEY (`ID_usuario1`)
    REFERENCES `sharing_books`.`usuario` (`ID_usuario`),
  CONSTRAINT `FK_usuario2`
    FOREIGN KEY (`ID_usuario2`)
    REFERENCES `sharing_books`.`usuario` (`ID_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
