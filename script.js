
```js
// No JavaScript is strictly necessary for this basic portfolio,
// but you could add interactive features here if needed.
// For example, smooth scrolling for navigation links:

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
```