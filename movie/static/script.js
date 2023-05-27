const form = document.querySelector('#recommendation-form');
const list = document.querySelector('#recommendation-list');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const movieName = e.target.elements.movie_name.value;
  fetch(`/recommend/?movie_name=${movieName}`)
    .then(response => response.json())
    .then(data => {
      const recommendations = data.recommendations;
      list.innerHTML = '';
      if (recommendations.length > 0) {
        recommendations.forEach(movie => {
          const li = document.createElement('li');
          li.textContent = movie;
          list.appendChild(li);
        });
      } else {
        const li = document.createElement('li');
        li.textContent = 'No recommendations found.';
        list.appendChild(li);
      }
    })
    .catch(error => console.error(error));
});
