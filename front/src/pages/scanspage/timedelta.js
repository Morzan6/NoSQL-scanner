export default function formatTimeDelta(inputTime) {
  const currentTime = new Date();
  const inputDate = new Date(inputTime);

  const timeDifference = currentTime - inputDate;

  const seconds = Math.floor(timeDifference / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (seconds < 60) {
    return seconds + " сек. назад";
  } else if (minutes < 60) {
    return minutes + " мин. назад";
  } else if (hours < 24) {
    return hours + " ч. назад";
  } else {
    return days + " дн. назад";
  }
}
