function initSlideshow() {
    let currentSlide = 0;
    const slides = document.querySelectorAll("#slideshow .slide");
    const numberOfSlides = slides.length;

    function showSlide() {
        // 全てのスライドを非表示
        slides.forEach(slide => slide.classList.remove('active'));

        // 現在のスライドを表示
        slides[currentSlide].classList.add('active');

        // 次のスライドに移動、または最初に戻る
        currentSlide = (currentSlide + 1) % numberOfSlides;
    }

    // 3秒ごとにスライドを切り替える
    setInterval(showSlide, 4000);
}

window.addEventListener('DOMContentLoaded', (event) => {
    initSlideshow();
});
