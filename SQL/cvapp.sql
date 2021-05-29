-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 30 May 2021, 00:06:48
-- Sunucu sürümü: 10.4.18-MariaDB
-- PHP Sürümü: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `cvapp`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_adsoyad` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `admin_eposta` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `admin_password` varchar(300) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_adsoyad`, `admin_eposta`, `admin_password`) VALUES
(7, 'KaptanTR', 'admin@kaptantr.com', 'f0cee3d3fd4815618262ca4a9667ae7c618c58e9a438defe67fd538fd96156d0');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ayarlar`
--

CREATE TABLE `ayarlar` (
  `ayar_baslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `ayar_altbaslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `ayar_anahtar` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `ayar_bakim` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `ayarlar`
--

INSERT INTO `ayarlar` (`ayar_baslik`, `ayar_altbaslik`, `ayar_anahtar`, `ayar_bakim`) VALUES
('Blog', 'Blog Açıklama', 'Blog Anahtar Kelime', 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `deneyimler`
--

CREATE TABLE `deneyimler` (
  `deneyim_id` int(11) NOT NULL,
  `deneyim_baslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `deneyim_altbaslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `deneyim_detay` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `deneyim_baslangic` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `deneyim_bitis` varchar(300) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `deneyimler`
--

INSERT INTO `deneyimler` (`deneyim_id`, `deneyim_baslik`, `deneyim_altbaslik`, `deneyim_detay`, `deneyim_baslangic`, `deneyim_bitis`) VALUES
(2, 'Deneyim Başlık 1', 'Deneyim Alt Başlık 1', 'Deneyim Detay 1', '2021-05-29', '2021-05-30'),
(3, 'Deneyim Başlık 2', 'Deneyim Alt Başlık 2', 'Deneyim Detay 2', '2021-05-29', '2021-05-30');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `egitimler`
--

CREATE TABLE `egitimler` (
  `egitim_id` int(11) NOT NULL,
  `egitim_baslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `egitim_altbaslik` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `egitim_detay` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `egitim_baslangic` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `egitim_bitis` varchar(300) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `egitimler`
--

INSERT INTO `egitimler` (`egitim_id`, `egitim_baslik`, `egitim_altbaslik`, `egitim_detay`, `egitim_baslangic`, `egitim_bitis`) VALUES
(5, 'Eğitim Başlık 1', 'Eğitim Alt Başlık 1', 'Eğitim Detay 1', '2021-05-29', '2021-05-30'),
(6, 'Eğitim Başlık 2', 'Eğitim Alt Başlık 2', 'Eğitim Detay 2', '2021-05-29', '2021-05-30');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hakkinda`
--

CREATE TABLE `hakkinda` (
  `hakkinda_ad` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_soyad` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_eposta` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_telefon` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_ulke` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_sehir` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_adres` varchar(500) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_resim` varchar(500) COLLATE utf8_turkish_ci NOT NULL,
  `hakkinda_detay` text COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `hakkinda`
--

INSERT INTO `hakkinda` (`hakkinda_ad`, `hakkinda_soyad`, `hakkinda_eposta`, `hakkinda_telefon`, `hakkinda_ulke`, `hakkinda_sehir`, `hakkinda_adres`, `hakkinda_resim`, `hakkinda_detay`) VALUES
('Kaptan', 'TR', 'admin@kaptantr.com', '0555555555', 'Türkiye', 'İstanbul', 'Türkiye', 'vesikalk.jpg', 'Açıklama ');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sosyalmedya`
--

CREATE TABLE `sosyalmedya` (
  `sosyal_facebook` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `sosyal_twitter` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `sosyal_instagram` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `sosyal_linkedin` varchar(300) COLLATE utf8_turkish_ci NOT NULL,
  `sosyal_github` varchar(300) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `sosyalmedya`
--

INSERT INTO `sosyalmedya` (`sosyal_facebook`, `sosyal_twitter`, `sosyal_instagram`, `sosyal_linkedin`, `sosyal_github`) VALUES
('https://tr-tr.facebook.com', 'https://twitter.com', 'https://instagram.com', 'https://linkedin.com', 'https://github.com');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yetenekler`
--

CREATE TABLE `yetenekler` (
  `yetenek_id` int(11) NOT NULL,
  `yetenek_ad` varchar(300) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yetenekler`
--

INSERT INTO `yetenekler` (`yetenek_id`, `yetenek_ad`) VALUES
(6, 'Yetenek 1'),
(7, 'Yetenek 2');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Tablo için indeksler `deneyimler`
--
ALTER TABLE `deneyimler`
  ADD PRIMARY KEY (`deneyim_id`);

--
-- Tablo için indeksler `egitimler`
--
ALTER TABLE `egitimler`
  ADD PRIMARY KEY (`egitim_id`);

--
-- Tablo için indeksler `yetenekler`
--
ALTER TABLE `yetenekler`
  ADD PRIMARY KEY (`yetenek_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `deneyimler`
--
ALTER TABLE `deneyimler`
  MODIFY `deneyim_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `egitimler`
--
ALTER TABLE `egitimler`
  MODIFY `egitim_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `yetenekler`
--
ALTER TABLE `yetenekler`
  MODIFY `yetenek_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
