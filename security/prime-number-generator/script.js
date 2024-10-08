const gridContainer = document.getElementById('grid');
    const gridSlider = document.getElementById('gridSlider');
    const numSlider = document.getElementById('numSlider');
    const baseSlider = document.getElementById('baseSlider');
    const baseNumberIncrementCheckbox = document.getElementById('baseNumberIncrementCheckbox');

    // Function to determine if a number is prime
    function isPrime(num) {
      if (num < 2) return false;
      for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
      }
      return true;
    }

    // Special primes: Twin primes (pairs of primes differing by 2)
    function isSpecialPrime(num) {
      return isPrime(num) && (isPrime(num - 2) || isPrime(num + 2));
    }

    // Convert number to selected base system
    function convertToBase(num, base) {
      return num.toString(base).toUpperCase();
    }

    // Generate the grid with numbers from 1 to numMax and in the selected base
    function generateGrid(size, numMax, base) {
      gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
      gridContainer.innerHTML = '';

      let currentMaxDigit = 0; // Initialize current max digit

      for (let i = 1; i <= numMax; i++) {
        const numberDiv = document.createElement('div');
        const convertedNumber = convertToBase(i, base);
        numberDiv.textContent = convertedNumber;
        numberDiv.classList.add('number');

        // Check if we have moved to a new digit in the current base
        const newDigit = Math.floor((i - 1) / base);
        if (newDigit > currentMaxDigit && baseNumberIncrementCheckbox.checked) {
          currentMaxDigit = newDigit;
          numberDiv.classList.add(`new-digit`); // Add new class for the digit level
          numberDiv.classList.add(`new-digit-${newDigit + 1}`); // Add new class for the digit level
        }

        // Add special classes for prime numbers
        if (isSpecialPrime(i)) {
          numberDiv.classList.add('special-prime');
        } else if (isPrime(i)) {
          numberDiv.classList.add('prime');
        } else {
          numberDiv.classList.add('non-prime');
        }

        gridContainer.appendChild(numberDiv);
      }
    }

    // Update grid when the sliders are adjusted
    function updateGrid() {
      const gridSize = gridSlider.value;
      const numMax = numSlider.value;
      const base = baseSlider.value;
      generateGrid(gridSize, numMax, base);
    }

    // Initial grid generation
    updateGrid();