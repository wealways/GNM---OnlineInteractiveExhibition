export default function timeForToday(value) {
  const today = new Date();
  const timeValue = new Date(value);
  
  const betweenTime = Math.floor((today.getTime() - timeValue.getTime()) / 1000 / 60);
  if (betweenTime < 1) return '방금 전';
  if (betweenTime < 60) {
      return `${betweenTime}분 전`;
  }

  const betweenTimeHour = Math.floor(betweenTime / 60);
  if (betweenTimeHour < 24) {
      return `${betweenTimeHour}시간 전`;
  }

  const betweenTimeDay = Math.floor(betweenTime / 60 / 24);
  // getMonth() : 0 ~ 11 따라서 + 1 해줘야 한다
  if (betweenTimeDay < 30) {
      return `${betweenTimeDay}일전`;
  } else { return `${timeValue.getFullYear()}.${timeValue.getMonth() + 1}.${timeValue.getDay()}`; }
  
  
}