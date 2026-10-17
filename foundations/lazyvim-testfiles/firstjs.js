/**
 * Test script for program runners.
 * Safe, self-contained, and uses standard console outputs.
 */

console.log("--- Program Runner Test Start ---");

// 1. Basic Output Test
console.log("Status: Success");

// 2. Environment / Time Test
const now = new Date();
console.log(`Current Timestamp: ${now.toISOString()}`);

// 3. Simple Logic & Math Test
function testAddition(a, b) {
    return a + b;
}

const num1 = 5;
const num2 = 10;
const result = testAddition(num1, num2);

console.log(`Math Check: ${num1} + ${num2} = ${result}`);

if (result === 15) {
    console.log("Logic Check: PASSED");
} else {
    console.log("Logic Check: FAILED");
}

console.log("--- Program Runner Test End ---");
