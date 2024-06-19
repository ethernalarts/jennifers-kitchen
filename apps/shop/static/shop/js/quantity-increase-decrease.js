
// set the target element of the input field
const $targetEl = document.getElementById('quantity-input');

// optionally set the increment and decrement elements
const $incrementEl = document.getElementById('increment-button');

const $decrementEl = document.getElementById('decrement-button');

// optional options with default values and callback functions
const options = {
    minValue: 1,
    maxValue: 20, // infinite
    onIncrement: () => {
        console.log('input field value has been incremented');
    },
    onDecrement: () => {
        console.log('input field value has been decremented');
    }
};

const instanceOptions = {
  id: 'quantity-input',
  override: true
};