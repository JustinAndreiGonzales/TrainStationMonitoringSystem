export function formatDateTime(datetimeString: string): { time: string, date: string } {
    const fullDate = new Date(datetimeString);

    const time = new Intl.DateTimeFormat("en-US", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: true
    });
    const formattedTime = time.format(fullDate);

    // Format date as "dd MMM yyyy"
    const date = new Intl.DateTimeFormat("en-GB", {
        day: "2-digit",
        month: "short",
        year: "numeric"
    });
    const formattedDate = date.format(fullDate);

    return { time: formattedTime, date: formattedDate };
}
