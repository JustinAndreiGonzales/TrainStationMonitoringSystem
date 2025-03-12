<script>
  import ApexChart from "svelte-apexcharts";

  export let series;
  export let categories;

  const options = {
    chart: {
      type: "bar",
      height: 320,
      fontFamily: "Inter, sans-serif",
      toolbar: { show: false },
    },
    colors: ["#1A56DB", "#FDBA8C"],
    plotOptions: {
      bar: { horizontal: false, columnWidth: "70%", borderRadius: 8 },
    },
    tooltip: { shared: true, intersect: false },
    states: { hover: { filter: { type: "darken", value: 1 } } },
    stroke: { show: true, width: 0, colors: ["transparent"] },
    grid: { show: false, strokeDashArray: 4, padding: { left: 2, right: 2, top: -14 } },
    dataLabels: { enabled: false },
    legend: { show: false },
    xaxis: {
      labels: {
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: "text-xs font-normal text-gray-500 dark:text-gray-400",
        },
      },
      axisBorder: { show: false },
      axisTicks: { show: false },
    },
    yaxis: { show: false },
    fill: { opacity: 1 },
  };
</script>

<ApexChart type="bar" {options} {series} {categories} height="320" />
