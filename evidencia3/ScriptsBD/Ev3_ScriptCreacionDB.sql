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
  `altura` INT NOT NULL,
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
  `hashed_password` VARCHAR(70) NOT NULL,
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
AUTO_INCREMENT = 12
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
  `ipAddress` VARCHAR(45) NULL DEFAULT NULL,
  `deviceInfo` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_usuarioLogueado` (`usuarioLogueado` ASC) VISIBLE,
  INDEX `idx_fechaIngreso` (`fechaIngreso` ASC) VISIBLE,
  CONSTRAINT `acceso_ibfk_1`
    FOREIGN KEY (`usuarioLogueado`)
    REFERENCES `sharing_books`.`usuario` (`ID_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 43
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
  `ID_libro1` INT NOT NULL,
  `ID_usuario2` INT NULL DEFAULT NULL,
  `ID_libro2` INT NOT NULL,
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

USE `sharing_books` ;

-- -----------------------------------------------------
-- Placeholder table for view `sharing_books`.`v_accesos_frecuentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`v_accesos_frecuentes` (`usuarioLogueado` INT, `numero_accesos` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sharing_books`.`v_intercambios_recientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`v_intercambios_recientes` (`id_usuario1` INT, `id_usuario2` INT, `fecha_intercambio` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sharing_books`.`v_usuarios_mas_libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharing_books`.`v_usuarios_mas_libros` (`ID_usuario` INT, `nombre_usuario` INT, `cantidad_libros` INT);

-- -----------------------------------------------------
-- View `sharing_books`.`v_accesos_frecuentes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sharing_books`.`v_accesos_frecuentes`;
USE `sharing_books`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `sharing_books`.`v_accesos_frecuentes` AS select `sharing_books`.`acceso`.`usuarioLogueado` AS `usuarioLogueado`,count(0) AS `numero_accesos` from `sharing_books`.`acceso` group by `sharing_books`.`acceso`.`usuarioLogueado` order by `numero_accesos` desc;

-- -----------------------------------------------------
-- View `sharing_books`.`v_intercambios_recientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sharing_books`.`v_intercambios_recientes`;
USE `sharing_books`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `sharing_books`.`v_intercambios_recientes` AS select `sharing_books`.`intercambio`.`ID_usuario1` AS `id_usuario1`,`sharing_books`.`intercambio`.`ID_usuario2` AS `id_usuario2`,`sharing_books`.`intercambio`.`fecha_intercambio` AS `fecha_intercambio` from `sharing_books`.`intercambio` order by `sharing_books`.`intercambio`.`fecha_intercambio` desc;

-- -----------------------------------------------------
-- View `sharing_books`.`v_usuarios_mas_libros`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sharing_books`.`v_usuarios_mas_libros`;
USE `sharing_books`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `sharing_books`.`v_usuarios_mas_libros` AS select `u`.`ID_usuario` AS `ID_usuario`,`u`.`nombre_usuario` AS `nombre_usuario`,count(`l`.`ID_libro`) AS `cantidad_libros` from (`sharing_books`.`usuario` `u` left join `sharing_books`.`libro` `l` on((`u`.`ID_usuario` = `l`.`ID_usuario`))) group by `u`.`ID_usuario` order by `cantidad_libros` desc;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
