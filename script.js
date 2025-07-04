const listContainer = document.getElementById("chapter-list");
const contentArea = document.getElementById("chapter-content");
const titleArea = document.querySelector("#content h1");

fetch("chapters.json")
  .then(res => res.json())
  .then(chapters => {
    chapters.forEach((chap, idx) => {
      const li = document.createElement("li");
      const btn = document.createElement("button");
      btn.textContent = chap.title;
      btn.addEventListener("click", () => {
        loadChapter(chap.filename, chap.title);
        setActiveButton(idx);
      });
      li.appendChild(btn);
      listContainer.appendChild(li);
    });

    // Auto-load first chapter
    if (chapters.length > 0) {
      loadChapter(chapters[0].filename, chapters[0].title);
      setActiveButton(0);
    }
  })
  .catch(err => {
    console.error("❌ Failed to load chapters.json:", err);
    contentArea.innerHTML = `<p style="color:red;">Unable to load chapters list.</p>`;
  });

function loadChapter(filename, title) {
  fetch(filename)
    .then(res => {
      if (!res.ok) throw new Error(`Failed to load chapter file: ${res.status}`);
      return res.text();
    })
    .then(html => {
      titleArea.textContent = title;
      contentArea.innerHTML = html;
    })
    .catch(err => {
      console.error(`❌ Error loading chapter "${title}":`, err);
      contentArea.innerHTML = `<p style="color:red;">Failed to load "${title}".</p>`;
    });
}

function setActiveButton(index) {
  const buttons = document.querySelectorAll("#chapter-list button");
  buttons.forEach((btn, i) => {
    btn.classList.toggle("active", i === index);
  });
}
