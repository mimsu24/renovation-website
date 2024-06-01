// Toggle for the navbar menu
const toggleButton = document.querySelector('.toggle-button');
const navbarLinks = document.querySelector('.navbar-links');

toggleButton.addEventListener('click', (event) => {
    navbarLinks.classList.toggle('active');
    event.preventDefault();
});

// Toggle sticky properties for navbar when scrolling, so that it sticks to the top of the screen
window.addEventListener('scroll', () => {
    const navBar = document.querySelector('.navbar');
    if (window.scrollY > 0) {
      navBar.classList.add('sticky');
    } else {
      navBar.classList.remove('sticky');
    }
  });
