document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('nav a');

  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      navLinks.forEach(link => link.classList.remove('active'));
      this.classList.add('active');
    });
  });

  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', async function(event) {
      event.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, message })
      });
      const data = await response.json();
      document.getElementById('response-message').innerText = data.message;
    });
  }

  const symptomForm = document.getElementById('symptom-form');
  if (symptomForm) {
    symptomForm.addEventListener('submit', async function(event) {
      event.preventDefault();
      const symptoms = document.getElementById('symptoms').value.split(',').map(s => s.trim());
      const response = await fetch('/api/diagnosis', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: symptoms.map(name => ({ name })) })
      });
      const data = await response.json();
      document.getElementById('recommendation').innerText = data.recommendation;
    });
  }

  const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
  smoothScrollLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
});
