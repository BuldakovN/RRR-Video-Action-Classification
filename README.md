<div align="center">
  
# ЦИФРОВОЙ ПРОРЫВ: СЕЗОН ИИ <br> Распознавание действий человека по видео

<img height="300" alt="logo" src="assets/logo1.png">

</div> 


## Оглавление
- ### [Задание](#1)
- ### [Решение](#2)
- ### [Запуск кода](#3)
- ### [Уникальность нашего решения](#4)
- ### [Стек](#5)
- ### [Команда](#6)
- ### [Ссылки](#7)

## <a name="1"> Задание </a>

Видеосъемка рабочего времени является методом исследования производственных процессов, трудовых операций и фактических затрат рабочего времени. Этот метод не только обеспечивает высокую точность измерения всех фактических затрат рабочего времени, но и любых трудовых операций и действий. В среднем в год по всей сети железных дорог инженерами по организации и нормированию труда структурных предприятий функциональных филиалов ОАО «РЖД» пересматривается или разрабатывается более 800 производственных процессов. Следовательно, автоматизации подобных рутинных процессов является актуальной задачей, а использование технологий искусственного интеллекта может стать эффективным решением.

Участникам хакатона предстоит разработать решение, которое позволит точно распознавать действия человека по видео с высокой быстродействием и надежностью. Решение должно автоматически распознавать и классифицировать различные действия человека на видео. Дополнительная задача - разработка пользовательского интерфейса для визуализации результатов распознавания действий человека.

## <a name="2">Решение </a>

### Архетиктура решения

<div align="center">
<img height="300" alt="logo" src="assets/deploy.drawio.png">

**Развертывание модели**
</div> 

### Архетиктура модели

<div align="center"><img height="200" alt="модель" src="assets/model_white.png"></div>

## <a name="3">Запуск кода </a>

### Последовательные шаги для запуска кода:
1. Склонируйте гит репозиторий;
```Bash
git clone https://github.com/BuldakovN/RRR-Video-Action-Classification.git
```
2. Скачайте веса для модели детекции https://drive.google.com/drive/folders/1iQRcneyDnb3q7LZ9wcGfkDt3W5zAKjwD?usp=sharing и разместите их в папках ```model/weights``` и ```modelStream/weights```

3. Запуск контейнеров и сервера стриминга:
```Bash
cd RRR-Video-Action-Classification
docker-compose build
docker-compose up

cd modelStream

pip3 install -r requirements.txt
python3 serverStream.py
```

## <a name="4">Уникальность нашего решения </a>

1. Возможность распознавания действий нескольких людей на одном кадре.

2. Работает в режиме реального времени.

3. Модель была предобучена на большом датасете.

4. Удобный веб-интерфейс для работы с моделью.

## <a name="5">Стек </a>
<div align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pytorch/pytorch-original.svg" title="Pytorch" alt="Pytorch" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/numpy/numpy-original.svg" title="Numpy" alt="Numpy" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/opencv/opencv-original.svg" title="OpenCV" alt="OpenCV" height="40"/>&nbsp;
  
  <img src="https://pjreddie.com/media/image/yologo_2.png" title="Yolo" alt="Yolo" height="40"/>&nbsp;
  <img src="https://spacenil.com/tutorial/public/uploads/categories/categories_1599665107.png" title="JS" alt="JS"  height="40"/>&nbsp;
  <img src="https://fronty.com/static/uploads/1.11-30.11/languages%20in%202022/go.png" title="GO" alt="GO" height="40"/>&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg"  title="Flask" alt="Flask" height="40"/>
</div>

## <a name="6">Команда </a>

*Состав команды "Оседлавшие тильт"*   

- <h4><img align="center" height="25" src="https://user-images.githubusercontent.com/51875349/198863127-837491f2-b57f-4c75-9840-6a4b01236c7a.png">: @Ubludor, Маслов Денис - Fullstack-developer</h3>
- <h4><img align="center" height="25" src="https://user-images.githubusercontent.com/51875349/198863127-837491f2-b57f-4c75-9840-6a4b01236c7a.png">: @BuldakovN, Булдаков Никита - CV-engineer</h3>
- <h4><img align="center" height="25" src="https://user-images.githubusercontent.com/51875349/198863127-837491f2-b57f-4c75-9840-6a4b01236c7a.png">: @ilkorotkov, Коротков Илья - CV-engineer</h3>
- <h4><img align="center" height="25" src="https://user-images.githubusercontent.com/51875349/198863127-837491f2-b57f-4c75-9840-6a4b01236c7a.png">: @Skadar7, Кузнецов Денис - CV-engineer</h3>
- <h4><img align="center" height="25" src="https://user-images.githubusercontent.com/51875349/198863127-837491f2-b57f-4c75-9840-6a4b01236c7a.png">: @Llaceyne, Гулария Лана - Designer, Frontend-developer</h3>

## <a name="7">Ссылки </a>

- [ссылка на веса модели детекции](https://drive.google.com/drive/folders/1iQRcneyDnb3q7LZ9wcGfkDt3W5zAKjwD?usp=sharing)&nbsp;
- [ссылка на скринкаст](https://drive.google.com/file/d/1Md4uNQFHtO_w9xxaigyc6ftbF0Tru6qk/view?usp=sharing)&nbsp;
