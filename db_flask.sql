-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 02 Jul 2024 pada 12.01
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_flask`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `articles`
--

CREATE TABLE `articles` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug_title` char(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` enum('published','draft') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `articles`
--

INSERT INTO `articles` (`id`, `user_id`, `category_id`, `title`, `slug_title`, `content`, `status`, `image`, `created_at`, `updated_at`, `deleted_at`) VALUES
(5, 1, 15, 'contoh', 'contoh', '                                <p>asa</p>\r\n                            ', 'published', 'beasiswa-01.png', '2024-07-01 17:22:27', '2024-07-01 17:22:44', NULL),
(6, 1, 1, 'asa ini adalah coao kk oa', 'asa-ini-adalah-c', '<p>lorem ipsum daleka oko a</p>', 'published', 'black-01.png', '2024-07-01 17:35:03', '2024-07-01 17:35:03', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `categories`
--

CREATE TABLE `categories` (
  `id` bigint(20) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug_name` char(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `categories`
--

INSERT INTO `categories` (`id`, `parent_id`, `name`, `slug_name`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, NULL, 'Artikel', 'artikel', '2024-05-24 23:28:52', '2024-07-01 17:22:06', NULL),
(15, NULL, 'Berita', 'berita', '2024-06-11 16:54:10', '2024-06-11 16:54:10', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `contents`
--

CREATE TABLE `contents` (
  `id` bigint(20) NOT NULL,
  `app_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `app_description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `app_logo` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `dictionaries`
--

CREATE TABLE `dictionaries` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug_name` char(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `dictionaries`
--

INSERT INTO `dictionaries` (`id`, `name`, `slug_name`, `description`, `image`, `created_at`, `updated_at`, `deleted_at`) VALUES
(3, 'A', 'a', 'Ini Adalah A', 'A.png', '2024-05-29 03:10:03', '2024-07-01 17:28:42', NULL),
(4, 'B', 'b', 'Ini B', 'B.png', '2024-06-02 11:09:02', '2024-07-01 17:28:49', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` char(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` datetime DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `phone`, `email_verified_at`, `password`, `remember_token`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Test User', 'admin@gmail.com', '62123456789', '2024-05-29 13:36:09', 'scrypt:32768:8:1$WAUcm6mmlZt39vQs$e11902afb00ed6ed0c1891a3a4f6a02fff996408a8c9103419622d69f4a9cf1799b3ae53b76f785448174f53db31165298f735a20152c89c24ce3dbd50530bc6', NULL, '2024-05-29 13:36:09', '2024-05-29 13:36:09', NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_articles_users` (`user_id`),
  ADD KEY `fk_articles_categories` (`category_id`);

--
-- Indeks untuk tabel `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `contents`
--
ALTER TABLE `contents`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `dictionaries`
--
ALTER TABLE `dictionaries`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_users_email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `articles`
--
ALTER TABLE `articles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `categories`
--
ALTER TABLE `categories`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT untuk tabel `contents`
--
ALTER TABLE `contents`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `dictionaries`
--
ALTER TABLE `dictionaries`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `articles`
--
ALTER TABLE `articles`
  ADD CONSTRAINT `fk_articles_categories` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  ADD CONSTRAINT `fk_articles_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
