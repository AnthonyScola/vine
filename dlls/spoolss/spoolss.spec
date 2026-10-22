@ stdcall AbortPrinter(long) winspool.drv.AbortPrinter
@ stdcall AddFormW(long long ptr) winspool.drv.AddFormW
@ stdcall AddJobW(long long ptr long ptr) winspool.drv.AddJobW
@ stdcall AddMonitorW(wstr long ptr)
@ stub AddPerMachineConnectionW
@ stdcall AddPortExW(wstr long ptr wstr) winspool.drv.AddPortExW
@ stdcall AddPortW(wstr long wstr) winspool.drv.AddPortW
@ stdcall AddPrintProcessorW(wstr wstr wstr wstr) winspool.drv.AddPrintProcessorW
@ stdcall AddPrintProvidorW(wstr long ptr) winspool.drv.AddPrintProvidorW
@ stdcall AddPrinterConnectionW(wstr) winspool.drv.AddPrinterConnectionW
@ stdcall AddPrinterDriverExW(wstr long ptr long)
@ stdcall AddPrinterDriverW(wstr long ptr) winspool.drv.AddPrinterDriverW
@ stub AddPrinterExW
@ stdcall AddPrinterW(wstr long ptr) winspool.drv.AddPrinterW
@ stdcall AllocSplStr(wstr)
@ stub AppendPrinterNotifyInfoData
@ stdcall BuildOtherNamesFromMachineName(ptr ptr)
@ stub CallDrvDevModeConversion
@ stub CallRouterFindFirstPrinterChangeNotification
@ stdcall ClosePrinter(long) winspool.drv.ClosePrinter
@ stub ClusterSplClose
@ stub ClusterSplIsAlive
@ stub ClusterSplOpen
@ stdcall ConfigurePortW(wstr long wstr) winspool.drv.ConfigurePortW
@ stub CreatePrinterIC
@ stub DbgGetPointers
@ stdcall DeleteFormW(long wstr) winspool.drv.DeleteFormW
@ stdcall DeleteMonitorW(wstr wstr wstr)
@ stub DeletePerMachineConnectionW
@ stdcall DeletePortW(wstr long wstr) winspool.drv.DeletePortW
@ stdcall DeletePrintProcessorW(wstr wstr wstr) winspool.drv.DeletePrintProcessorW
@ stdcall DeletePrintProvidorW(wstr wstr wstr) winspool.drv.DeletePrintProvidorW
@ stdcall DeletePrinter(long) winspool.drv.DeletePrinter
@ stdcall DeletePrinterConnectionW(wstr) winspool.drv.DeletePrinterConnectionW
@ stdcall DeletePrinterDataExW(long wstr wstr) winspool.drv.DeletePrinterDataExW
@ stub DeletePrinterDataW
@ stdcall DeletePrinterDriverExW(wstr wstr wstr long long) winspool.drv.DeletePrinterDriverExW
@ stdcall DeletePrinterDriverW(wstr wstr wstr) winspool.drv.DeletePrinterDriverW
@ stub DeletePrinterIC
@ stub DeletePrinterKeyW
@ stdcall DllAllocSplMem(long)
@ stdcall DllFreeSplMem(ptr)
@ stdcall DllFreeSplStr(wstr)
@ stdcall EndDocPrinter(long) winspool.drv.EndDocPrinter
@ stdcall EndPagePrinter(long) winspool.drv.EndPagePrinter
@ stdcall EnumFormsW(long long ptr long ptr ptr) winspool.drv.EnumFormsW
@ stdcall EnumJobsW(long long long long ptr long ptr ptr) winspool.drv.EnumJobsW
@ stdcall EnumMonitorsW(wstr long ptr long ptr ptr)
@ stub EnumPerMachineConnectionsW
@ stdcall EnumPortsW(wstr long ptr long ptr ptr)
@ stdcall EnumPrintProcessorDatatypesW(wstr wstr long ptr long ptr ptr) winspool.drv.EnumPrintProcessorDatatypesW
@ stdcall EnumPrintProcessorsW(wstr wstr long ptr long ptr ptr) winspool.drv.EnumPrintProcessorsW
@ stdcall EnumPrinterDataExW(long wstr ptr long ptr ptr) winspool.drv.EnumPrinterDataExW
@ stdcall EnumPrinterDataW(long long ptr long ptr ptr ptr long ptr) winspool.drv.EnumPrinterDataW
@ stdcall EnumPrinterDriversW(wstr wstr long ptr long ptr ptr) winspool.drv.EnumPrinterDriversW
@ stdcall EnumPrinterKeyW(long wstr ptr long ptr) winspool.drv.EnumPrinterKeyW
@ stdcall EnumPrintersW(long ptr long ptr long ptr ptr) winspool.drv.EnumPrintersW
@ stdcall FindClosePrinterChangeNotification(long) winspool.drv.FindClosePrinterChangeNotification
@ stub FlushPrinter
@ stub FormatPrinterForRegistryKey
@ stub FormatRegistryKeyForPrinter
@ stub FreeOtherNames
@ stub GetClientUserHandle
@ stdcall GetFormW(long wstr long ptr long ptr) winspool.drv.GetFormW
@ stub GetJobAttributes
@ stdcall GetJobW(long long long ptr long ptr) winspool.drv.GetJobW
@ stub GetNetworkId
@ stdcall GetPrintProcessorDirectoryW(wstr wstr long ptr long ptr) winspool.drv.GetPrintProcessorDirectoryW
@ stdcall GetPrinterDataExW(long wstr wstr ptr ptr long ptr) winspool.drv.GetPrinterDataExW
@ stdcall GetPrinterDataW(long wstr ptr ptr long ptr) winspool.drv.GetPrinterDataW
@ stdcall GetPrinterDriverDirectoryW(wstr wstr long ptr long ptr)
@ stub GetPrinterDriverExW
@ stdcall GetPrinterDriverW(long wstr long ptr long ptr) winspool.drv.GetPrinterDriverW
@ stdcall GetPrinterW(long long ptr long ptr) winspool.drv.GetPrinterW
@ stdcall ImpersonatePrinterClient(long)
@ stdcall InitializeRouter()
@ stdcall IsLocalCall()
@ stub IsNamedPipeRpcCall
@ stub LoadDriver
@ stub LoadDriverFiletoConvertDevmode
@ stub MIDL_user_allocate1
@ stub MIDL_user_free1
@ stub MarshallDownStructure
@ stub MarshallUpStructure
@ stub OldGetPrinterDriverW
@ stub OpenPrinterExW
@ stub OpenPrinterPortW
@ stdcall OpenPrinterW(wstr ptr ptr) winspool.drv.OpenPrinterW
@ stub PackStrings
@ stub PartialReplyPrinterChangeNotification
@ stub PlayGdiScriptOnPrinterIC
@ stub PrinterHandleRundown
@ stub PrinterMessageBoxW
@ stub ProvidorFindClosePrinterChangeNotification
@ stub ProvidorFindFirstPrinterChangeNotification
@ stdcall ReadPrinter(long ptr long ptr) winspool.drv.ReadPrinter
@ stub ReallocSplMem
@ stub ReallocSplStr
@ stub RemoteFindFirstPrinterChangeNotification
@ stub ReplyClosePrinter
@ stub ReplyOpenPrinter
@ stub ReplyPrinterChangeNotification
@ stdcall ResetPrinterW(long ptr) winspool.drv.ResetPrinterW
@ stdcall RevertToPrinterSelf()
@ stub RouterAllocPrinterNotifyInfo
@ stub RouterFindFirstPrinterChangeNotification
@ stub RouterFindNextPrinterChangeNotification
@ stub RouterFreePrinterNotifyInfo
@ stub RouterRefreshPrinterChangeNotification
@ stub RouterReplyPrinter
@ stdcall ScheduleJob(long long) winspool.drv.ScheduleJob
@ stdcall SeekPrinter(long int64 ptr long long) winspool.drv.SeekPrinter
@ stub SetAllocFailCount
@ stdcall SetFormW(long wstr long ptr) winspool.drv.SetFormW
@ stdcall SetJobW(long long long ptr long) winspool.drv.SetJobW
@ stub SetPortW
@ stdcall SetPrinterDataExW(long wstr wstr long ptr long) winspool.drv.SetPrinterDataExW
@ stdcall SetPrinterDataW(long wstr long ptr long) winspool.drv.SetPrinterDataW
@ stdcall SetPrinterW(long long ptr long) winspool.drv.SetPrinterW
@ stub SplCloseSpoolFileHandle
@ stub SplCommitSpoolData
@ stub SplDriverUnloadComplete
@ stub SplGetSpoolFileInfo
@ stdcall SplInitializeWinSpoolDrv(ptr)
@ stdcall SplIsUpgrade()
@ stub SplProcessPnPEvent
@ stub SplReadPrinter
@ stub SplRegisterForDeviceEvents
@ stub SplStartPhase2Init
@ stub SplUnregisterForDeviceEvents
@ stub SpoolerFindClosePrinterChangeNotification
@ stub SpoolerFindFirstPrinterChangeNotification
@ stub SpoolerFindNextPrinterChangeNotification
@ stub SpoolerFreePrinterNotifyInfo
@ stdcall SpoolerHasInitialized()
@ stdcall SpoolerInit()
@ stdcall StartDocPrinterW(long long ptr) winspool.drv.StartDocPrinterW
@ stdcall StartPagePrinter(long) winspool.drv.StartPagePrinter
@ stub UnloadDriver
@ stub UnloadDriverFile
@ stub UpdateBufferSize
@ stub UpdatePrinterRegAll
@ stub UpdatePrinterRegUser
@ stub WaitForPrinterChange
@ stdcall WaitForSpoolerInitialization()
@ stdcall WritePrinter(long ptr long ptr) winspool.drv.WritePrinter
@ stdcall XcvDataW(long wstr ptr long ptr long ptr ptr) winspool.drv.XcvDataW
@ stub bGetDevModePerUser
@ stub bSetDevModePerUser
@ stub pszDbgAllocMsgA
@ stub vDbgLogError
