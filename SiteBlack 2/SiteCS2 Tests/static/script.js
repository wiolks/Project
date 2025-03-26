document.addEventListener('DOMContentLoaded', function() {
    const videoGrid = document.querySelector('.video-grid');
    const videoOverlay = document.getElementById('video-overlay');
    const videoPlayer = document.getElementById('video-player');
    const overlayVideoSource = document.getElementById('overlay-video-source');
    const videoDescription = document.getElementById('video-description');
    const closeButton = document.getElementById('close-button');

    videoGrid.addEventListener('click', function(event) {
        const videoItem = event.target.closest('.video-item'); // Найти ближайший .video-item
        if (videoItem) {
            const videoSrc = '/videos/' + videoItem.dataset.video;
            const description = videoItem.dataset.description;

            overlayVideoSource.src = videoSrc;
            videoPlayer.querySelector('video').load(); // Важно перезагрузить видео
            videoDescription.textContent = description;

            videoOverlay.classList.add('show'); // Добавить класс для анимации
        }
    });

    closeButton.addEventListener('click', function() {
        videoOverlay.classList.remove('show'); // Удалить класс для анимации
        videoPlayer.querySelector('video').pause(); // Остановить видео
    });

    videoOverlay.addEventListener('click', function(event) {
        if (event.target === videoOverlay) {
            videoOverlay.classList.remove('show'); // Удалить класс для анимации
            videoPlayer.querySelector('video').pause();
        }
    });
});