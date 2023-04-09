


function showDropdown(id) {
    document.getElementById(id + '-dropdown').classList.add('show');
  }

  function hideDropdown(id) {
    document.getElementById(id + '-dropdown').classList.remove('show');
  }


$(document).ready(function(){
    $('.parallax').parallax();
  });



  $(document).ready(function(){
    $('.parallax').parallax();
  });




// Получаем элементы, с которыми будем работать
const queueDropdown = document.getElementById("queue-dropdown");
const roomDropdown = document.getElementById("room-dropdown");
const areaSlider = document.getElementById("area-slider");

// Функция для обновления текста элемента
function updateText(element, text) {
  element.innerText = text;
}

// Обработчик события для изменения значения слайдера
areaSlider.oninput = function() {
  const areaText = document.getElementById("area-text");
  updateText(areaText, this.value + " - " + (this.value + 57) + " кв. м.");
}

// Инициализируем значения элементов
updateText(queueDropdown.querySelector(".af_item_text"), "Все очереди");
updateText(roomDropdown.querySelector(".af_item_text"), "Все варианты");
updateText(areaSlider, "22");

// Добавляем варианты в первый и второй блоки
const queueItems = ["вариант1", "вариант2", "вариант3"];
const roomItems = ["вариант1", "вариант2", "вариант3"];

for (let item of queueItems) {
  const newQueueItem = document.createElement("div");
  newQueueItem.classList.add("af_item");
  updateText(newQueueItem, item);
  queueDropdown.querySelector(".af_dropdown_scroll").appendChild(newQueueItem);
}

for (let item of roomItems) {
  const newRoomItem = document.createElement("div");
  newRoomItem.classList.add("af_item");
  updateText(newRoomItem, item);
  roomDropdown.querySelector(".af_dropdown_block").appendChild(newRoomItem);
}