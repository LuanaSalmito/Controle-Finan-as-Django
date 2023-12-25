function toggleActiveClass(element) {

    const hasActiveClass = element.classList.contains('active');

    if (hasActiveClass) {
      element.classList.remove('active');
    } else {
      element.classList.add('active');
    }
  }

  const menuToggle = document.querySelector('#menu-toggle');
  menuToggle.addEventListener('click', () => {
    
    toggleActiveClass(document.querySelector('#menu-mobile-toggle'));
    console.log("Oi");
  });