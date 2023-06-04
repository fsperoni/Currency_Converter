function goBack() {
  window.history.back()
}

function roundAmount() {
  const amtInput = document.getElementById("amount")
  const amt = parseFloat(amtInput.value).toFixed(2)
  amtInput.value = parseFloat(amt)
}