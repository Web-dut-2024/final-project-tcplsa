// 获取按钮元素
var backToTop = document.getElementById('backToTop');

// 为按钮添加点击事件监听器
backToTop.addEventListener('click', function() {
    // 当按钮被点击时，滚动到页面顶部
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // 平滑滚动

    });
});


