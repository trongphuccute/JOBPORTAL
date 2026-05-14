/* ================= BENEFIT ANIMATION ================= */

window.addEventListener("scroll", function () {
  const items = document.querySelectorAll(".benefit-item");

  items.forEach((item) => {
    const position = item.getBoundingClientRect().top;

    const screen = window.innerHeight;

    if (position < screen - 100) {
      item.classList.add("show");
    }
  });
});

/* ================= DOM LOADED ================= */

document.addEventListener("DOMContentLoaded", function () {
  /* ================= CHART ================= */

  const chartEl = document.getElementById("chart");

  if (chartEl) {
    const labels = JSON.parse(chartEl.dataset.labels || "[]");

    const data = JSON.parse(chartEl.dataset.data || "[]");

    const info = JSON.parse(chartEl.dataset.info || "[]");

    new Chart(chartEl, {
      type: "line",

      data: {
        labels: labels,

        datasets: [
          {
            label: "Applications",

            data: data,

            tension: 0.4,

            borderWidth: 3,

            pointRadius: 5,

            pointHoverRadius: 8,

            fill: true,
          },
        ],
      },

      options: {
        responsive: true,

        plugins: {
          legend: {
            display: false,
          },

          tooltip: {
            backgroundColor: "#0a4a3c",

            callbacks: {
              title: function (ctx) {
                const i = ctx[0].dataIndex;

                return "📅 " + info[i].date;
              },

              label: function (ctx) {
                const i = ctx.dataIndex;

                let text = "📄 " + info[i].total + " applications";

                if (info[i].jobs.length > 0) {
                  text += "\n- " + info[i].jobs.join("\n- ");
                }

                return text;
              },
            },
          },
        },

        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }

  /* ================= DASHBOARD TAB ================= */

  const menuItems = document.querySelectorAll(".menu li");

  const tabs = document.querySelectorAll(".tab");

  if (menuItems.length > 0) {
    menuItems.forEach((item) => {
      item.addEventListener("click", () => {
        /* remove active menu */

        menuItems.forEach((i) => i.classList.remove("active"));

        /* remove active tab */

        tabs.forEach((t) => t.classList.remove("active"));

        /* active menu */

        item.classList.add("active");

        /* show tab */

        const tabId = item.getAttribute("data-tab");

        const target = document.getElementById(tabId);

        if (target) {
          target.classList.add("active");
        }
      });
    });
  }
});

/* ================= GLASS NAVBAR ================= */

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".glass-navbar");

  if (!navbar) return;

  if (window.scrollY > 30) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});
/* ================= COUNTER ANIMATION ================= */

let counterStarted = false;

function startCounters() {
  if (counterStarted) return;

  const counters = document.querySelectorAll(".counter");
  console.log("Counter elements found:", counters.length);

  if (counters.length === 0) {
    console.log("No counters found!");
    return;
  }

  counters.forEach((counter, index) => {
    const target = parseInt(counter.getAttribute("data-target")) || 0;
    console.log(
      `Counter ${index}: target = ${target}, current text = ${counter.innerText}`,
    );

    let current = 0;
    const increment = Math.ceil(target / 100);

    const updateCounter = () => {
      if (current < target) {
        current += increment;
        if (current > target) current = target;
        counter.innerText = current.toLocaleString();
        setTimeout(updateCounter, 30);
      }
    };

    updateCounter();
  });

  counterStarted = true;
}

// Start immediately on page load
window.addEventListener("load", () => {
  console.log("Page loaded, starting counters");
  startCounters();
});

// Backup: try on DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM Content Loaded");
  setTimeout(() => {
    if (!counterStarted) {
      console.log("Starting counters from DOMContentLoaded");
      startCounters();
    }
  }, 100);
});

// Also trigger on scroll
window.addEventListener("scroll", () => {
  if (!counterStarted) {
    const heroStats = document.querySelector(".hero-stats");
    if (heroStats) {
      const position = heroStats.getBoundingClientRect().top;
      if (position < window.innerHeight) {
        console.log("Starting counters from scroll");
        startCounters();
      }
    }
  }
});
/* ================= REVEAL CARDS ================= */

const revealCards = document.querySelectorAll(".featured-job-card");

window.addEventListener("scroll", () => {
  revealCards.forEach((card) => {
    const top = card.getBoundingClientRect().top;

    if (top < window.innerHeight - 100) {
      card.classList.add("show-card");
    }
  });
});
// ================= WHY SECTION ANIMATION =================

const revealWhyCards = document.querySelectorAll(".reveal-card");

window.addEventListener("scroll", () => {
  revealWhyCards.forEach((card) => {
    const top = card.getBoundingClientRect().top;

    const screen = window.innerHeight;

    if (top < screen - 80) {
      card.classList.add("show");
    }
  });
});

const darkBtn = document.getElementById("darkModeToggle");

if(localStorage.getItem("darkMode") === "enabled"){

    document.body.classList.add("dark-mode");

    darkBtn.innerHTML = "☀️";
}

darkBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")){

        localStorage.setItem("darkMode","enabled");

        darkBtn.innerHTML = "<img src='{% static 'img/sun_icon.png' %}' alt='Light Mode' width='30'>";

    }else{

        localStorage.setItem("darkMode","disabled");

        darkBtn.innerHTML = "<img src='{% static 'img/moon_icon.png' %}' alt='Dark Mode' width='30'>";
    }

});
/* ================= BLOG FORM ================= */
function previewImage(file) {

    const preview = document.getElementById("imagePreview");

    if (file) {

        const reader = new FileReader();

        reader.onload = function (e) {
            preview.innerHTML = `
                <img src="${e.target.result}" alt="Preview">
            `;
        };

        reader.readAsDataURL(file);

    } else {
        preview.innerHTML = "";
    }
}

/* INPUT FILE CHANGE */
document.getElementById("id_image").addEventListener("change", function (event) {

    const file = event.target.files[0];
    previewImage(file);

});
const uploadArea = document.getElementById("uploadArea");

const imageInput = document.getElementById("id_image");

/* CLICK CHỌN FILE */

uploadArea.addEventListener("click", () => {

    imageInput.click();

});

/* DRAG OVER */

uploadArea.addEventListener("dragover", (e) => {

    e.preventDefault();

    uploadArea.classList.add("dragover");

});

/* DRAG LEAVE */

uploadArea.addEventListener("dragleave", () => {

    uploadArea.classList.remove("dragover");

});

/* DROP FILE */

uploadArea.addEventListener("drop", (e) => {

    e.preventDefault();

    uploadArea.classList.remove("dragover");

    const files = e.dataTransfer.files;

    if (files.length > 0) {

        imageInput.files = files;

        previewImage({

            target: {

                files: files

            }

        });

    }

});


/* DOM LOADED */
document.addEventListener("DOMContentLoaded", function () {

    const uploadArea = document.getElementById("uploadArea");
    const imageInput = document.getElementById("id_image");

    /* CLICK TO SELECT */
    uploadArea.addEventListener("click", () => {
        imageInput.click();
    });

    /* DRAG OVER */
    uploadArea.addEventListener("dragover", function (e) {

        e.preventDefault();
        uploadArea.classList.add("dragover");

    });

    /* DRAG LEAVE */
    uploadArea.addEventListener("dragleave", function () {

        uploadArea.classList.remove("dragover");

    });

    /* DROP FILE */
    uploadArea.addEventListener("drop", function (e) {

        e.preventDefault();

        uploadArea.classList.remove("dragover");

        const files = e.dataTransfer.files;

        if (files.length > 0) {

            imageInput.files = files;

            previewImage(files[0]);

        }
    });

});