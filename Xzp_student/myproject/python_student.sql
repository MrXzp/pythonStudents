/*
 Navicat Premium Data Transfer

 Source Server         : mysql8.0
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3307
 Source Schema         : python_student

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 28/04/2024 10:35:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色昵称',
  `sort` bigint(0) NULL DEFAULT 0 COMMENT '排序',
  `remarks` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL COMMENT '备注',
  `is_del` bigint(0) UNSIGNED NULL DEFAULT NULL,
  `ctime` bigint(0) NULL DEFAULT NULL,
  `utime` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20002 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (20001, '上帝', 0, '超级管理员', NULL, NULL, NULL);
INSERT INTO `role` VALUES (20002, '系统用户', 0, NULL, NULL, NULL, NULL);
INSERT INTO `role` VALUES (20003, '游客', 0, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `account` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '用户登录账号',
  `password` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '用户登录密码',
  `nick_name` varchar(191) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '默认用户' COMMENT '用户昵称',
  `phone` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '手机号',
  `email` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL COMMENT '邮箱地址',
  `is_del` bigint(0) UNSIGNED NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  `utime` datetime(0) NULL DEFAULT NULL,
  `role_id` bigint(0) NULL DEFAULT NULL COMMENT '角色id\r\n',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `account`(`account`) USING BTREE,
  INDEX `idx_user_account`(`account`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10002 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (10001, 'admin', '360121', '超级管理员', '18296642121', '974614985@qq.com', 20001, NULL, NULL, 20001);
INSERT INTO `user` VALUES (10002, 'liuc', '123456', '刘禅', '15777478591', '', 0, '2024-04-28 10:23:46', '2024-04-28 10:23:46', 20003);

SET FOREIGN_KEY_CHECKS = 1;
