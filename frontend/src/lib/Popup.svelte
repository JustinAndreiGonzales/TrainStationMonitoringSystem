<script>
    export let message = "";
  </script>
  
  <div
    class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 bg-red-600 text-white text-lg rounded-lg shadow-lg p-6 z-50"
    role="alert"
  >
    <div class="flex justify-between items-center">
      <span>{message}</span>
    </div>
  </div>
  