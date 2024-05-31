document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('.tab');
    const articlesContainer = document.getElementById('articles');

    tabs.forEach(tab => {
        tab.addEventListener('change', function () {
            const categoryId = this.getAttribute('data-category-id');
            fetchArticles(categoryId);
        });
    });

    function fetchArticles(categoryId) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/blog/fetch_articles', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.error) {
                    console.error(response.error);
                    return;
                }
                renderArticles(response.articles);
            } else {
                console.error('Error fetching articles:', xhr.statusText);
            }
        };

        xhr.onerror = function () {
            console.error('Request error...');
        };

        xhr.send(JSON.stringify({ category_id: categoryId }));
    }

    function renderArticles(articles) {
        articlesContainer.innerHTML = '';
        articles.forEach(article => {
            const articleElement = document.createElement('div');
            articleElement.classList.add('article');
            articleElement.setAttribute('data-category-id', article.category_id);

            // Create and append the image element
            const articleImage = document.createElement('img');
            articleImage.src = article.photo_url;
            articleImage.alt = article.title;
            articleElement.appendChild(articleImage);

            // Create and append the title element
            const articleTitle = document.createElement('h2');
            articleTitle.textContent = article.title;
            articleElement.appendChild(articleTitle);

            // Create and append the content element
            const articleContent = document.createElement('p');
            const words = article.content.split(' ');
            if (words.length > 30) {
                articleContent.textContent = words.slice(0, 30).join(' ') + '...';
            } else {
                articleContent.textContent = article.content;
            }
            articleElement.appendChild(articleContent);

            // Create and append the read more link
            const readMoreLink = document.createElement('a');
            readMoreLink.href = '/blog/article/' + article.id;
            readMoreLink.classList.add('read-more');
            readMoreLink.textContent = 'Read more';
            articleElement.appendChild(readMoreLink);

            // Append the article element to the articles container
            articlesContainer.appendChild(articleElement);
        });
    }
});






