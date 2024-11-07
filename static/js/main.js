// Countdown Timer
function updateCountdown() {
    const eventDate = new Date('2024-11-18T18:00:00-05:00');
    const now = new Date();
    const diff = eventDate - now;

    if (diff <= 0) {
        document.getElementById('countdown').innerHTML = 'Event has started!';
        return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    document.getElementById('countdown').innerHTML = 
        `${days}d ${hours}h ${minutes}m ${seconds}s until event starts`;
}

// Update countdown every second
setInterval(updateCountdown, 1000);
updateCountdown();

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Flash messages
const flashMessages = document.querySelectorAll('.alert');
flashMessages.forEach(message => {
    setTimeout(() => {
        message.classList.add('fade');
        setTimeout(() => message.remove(), 300);
    }, 3000);
});
