defineHandler({
  onEnter(log, args, state) {
    log('Sleep()');
    log('Sleep() - dwMilliseconds = ', args[0]);
    args[0] = ptr("0x02")
    log('Sleep() - dwMilliseconds = ', args[0]);      
  },

  onLeave(log, retval, state) {
  }
});
