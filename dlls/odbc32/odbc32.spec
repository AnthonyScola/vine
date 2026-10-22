  1 stdcall SQLAllocConnect(long ptr)
  2 stdcall SQLAllocEnv(ptr)
  3 stdcall SQLAllocStmt(long ptr)
  4 stdcall SQLBindCol(long long long ptr long ptr)
  5 stdcall SQLCancel(long)
  6 stdcall SQLColAttributes(long long long ptr long ptr ptr)
  7 stdcall SQLConnect(long str long str long str long)
  8 stdcall SQLDescribeCol(long long ptr long ptr ptr ptr ptr ptr)
  9 stdcall SQLDisconnect(long)
 10 stdcall SQLError(long long long ptr ptr ptr long ptr)
 11 stdcall SQLExecDirect(long str long)
 12 stdcall SQLExecute(long)
 13 stdcall SQLFetch(long)
 14 stdcall SQLFreeConnect(long)
 15 stdcall SQLFreeEnv(long)
 16 stdcall SQLFreeStmt(long long )
 17 stdcall SQLGetCursorName(long ptr long ptr)
 18 stdcall SQLNumResultCols(long ptr)
 19 stdcall SQLPrepare(long str long)
 20 stdcall SQLRowCount(long ptr)
 21 stdcall SQLSetCursorName(long str long)
 22 stdcall SQLSetParam(long long long long long long ptr ptr)
 23 stdcall SQLTransact(long long long)
 24 stdcall SQLAllocHandle(long long ptr)
 25 stdcall SQLBindParam(long long long long long long ptr ptr)
 26 stdcall SQLCloseCursor(long)
 27 stdcall SQLColAttribute(long long long ptr long ptr ptr)
 28 stdcall SQLCopyDesc(long long)
 29 stdcall SQLEndTran(long long long)
 30 stdcall SQLFetchScroll(long long long)
 31 stdcall SQLFreeHandle(long long)
 32 stdcall SQLGetConnectAttr(long long ptr long ptr)
 33 stdcall SQLGetDescField(long long long ptr long ptr)
 34 stdcall SQLGetDescRec(long long ptr long ptr ptr ptr ptr ptr ptr ptr)
 35 stdcall SQLGetDiagField(long long long long ptr long ptr)
 36 stdcall SQLGetDiagRec(long long long ptr ptr ptr long ptr)
 37 stdcall SQLGetEnvAttr(long long ptr long ptr)
 38 stdcall SQLGetStmtAttr(long long ptr long ptr)
 39 stdcall SQLSetConnectAttr(long long ptr long)
 40 stdcall SQLColumns(long str long str long str long str long)
 41 stdcall SQLDriverConnect(long long str long ptr long ptr long)
 42 stdcall SQLGetConnectOption(long long ptr)
 43 stdcall SQLGetData(long long long ptr long ptr)
 44 stdcall SQLGetFunctions(long long ptr)
 45 stdcall SQLGetInfo(long long ptr long ptr)
 46 stdcall SQLGetStmtOption(long long ptr)
 47 stdcall SQLGetTypeInfo(long long)
 48 stdcall SQLParamData(long ptr)
 49 stdcall SQLPutData(long ptr long)
 50 stdcall SQLSetConnectOption(long long long)
 51 stdcall SQLSetStmtOption(long long long)
 52 stdcall SQLSpecialColumns(long long str long str long str long long long)
 53 stdcall SQLStatistics(long str long str long str long long long)
 54 stdcall SQLTables(long str long str long str long str long)
 55 stdcall SQLBrowseConnect(long str long ptr long ptr)
 56 stdcall SQLColumnPrivileges(long str long str long str long str long)
 57 stdcall SQLDataSources(long long str long ptr ptr long ptr)
 58 stdcall SQLDescribeParam(long long ptr ptr ptr ptr)
 59 stdcall SQLExtendedFetch(long long long ptr ptr)
 60 stdcall SQLForeignKeys(long str long str long str long str long str long str long)
 61 stdcall SQLMoreResults(long)
 62 stdcall SQLNativeSql(long str long ptr long ptr)
 63 stdcall SQLNumParams(long ptr)
 64 stdcall SQLParamOptions(long long ptr)
 65 stdcall SQLPrimaryKeys(long str long str long str long)
 66 stdcall SQLProcedureColumns(long str long str long str long str long)
 67 stdcall SQLProcedures(long str long str long str long)
 68 stdcall SQLSetPos(long long long long)
 69 stdcall SQLSetScrollOptions(long long long long)
 70 stdcall SQLTablePrivileges(long str long str long str long)
 71 stdcall SQLDrivers(long long str long ptr ptr long ptr)
 72 stdcall SQLBindParameter(long long long long long long long ptr long ptr)
 73 stdcall SQLSetDescField(long long long ptr long)
 74 stdcall SQLSetDescRec(long long long long long long long ptr ptr ptr)
 75 stdcall SQLSetEnvAttr(long long ptr long)
 76 stdcall SQLSetStmtAttr(long long ptr long)
 77 stdcall SQLAllocHandleStd(long long ptr)
 78 stdcall SQLBulkOperations(long long)
 79 stub    CloseODBCPerfData
 80 stub    CollectODBCPerfData
 81 stub    CursorLibLockDbc
 82 stub    CursorLibLockDesc
 83 stub    CursorLibLockStmt
 84 stub    ODBCGetTryWaitValue
 85 stub    CursorLibTransact
 86 stub    ODBSetTryWaitValue
 89 stub    ODBCSharedPerfMon
 90 stub    ODBCSharedVSFlag
106 stdcall SQLColAttributesW(long long long ptr long ptr ptr)
107 stdcall SQLConnectW(long wstr long wstr long wstr long)
108 stdcall SQLDescribeColW(long long ptr long ptr ptr ptr ptr ptr)
110 stdcall SQLErrorW(long long long ptr ptr ptr long ptr)
111 stdcall SQLExecDirectW(long ptr long)
117 stdcall SQLGetCursorNameW(long ptr long ptr)
119 stdcall SQLPrepareW(long wstr long)
121 stdcall SQLSetCursorNameW(long wstr long)
127 stdcall SQLColAttributeW(long long long ptr long ptr ptr)
132 stdcall SQLGetConnectAttrW(long long ptr long ptr)
133 stdcall SQLGetDescFieldW(long long long ptr long ptr)
134 stdcall SQLGetDescRecW(long long ptr long ptr ptr ptr ptr ptr ptr ptr)
135 stdcall SQLGetDiagFieldW(long long long long ptr long ptr)
136 stdcall SQLGetDiagRecW(long long long ptr ptr ptr long ptr)
138 stdcall SQLGetStmtAttrW(long long ptr long ptr)
139 stdcall SQLSetConnectAttrW(long long ptr long)
140 stdcall SQLColumnsW(long wstr long wstr long wstr long wstr long)
141 stdcall SQLDriverConnectW(long long wstr long ptr long ptr long)
142 stdcall SQLGetConnectOptionW(long long ptr)
145 stdcall SQLGetInfoW(long long ptr long ptr)
147 stdcall SQLGetTypeInfoW(long long)
150 stdcall SQLSetConnectOptionW(long long long)
152 stdcall SQLSpecialColumnsW(long long wstr long wstr long wstr long long long)
153 stdcall SQLStatisticsW(long wstr long wstr long wstr long long long)
154 stdcall SQLTablesW(long wstr long wstr long wstr long wstr long)
155 stdcall SQLBrowseConnectW(long wstr long ptr long ptr)
156 stdcall SQLColumnPrivilegesW(long wstr long wstr long wstr long wstr long)
157 stdcall SQLDataSourcesW(long long wstr long ptr ptr long ptr)
160 stdcall SQLForeignKeysW(long wstr long wstr long wstr long wstr long wstr long wstr long)
162 stdcall SQLNativeSqlW(long wstr long ptr long ptr)
165 stdcall SQLPrimaryKeysW(long wstr long wstr long wstr long)
166 stdcall SQLProcedureColumnsW(long wstr long wstr long wstr long wstr long)
167 stdcall SQLProceduresW(long wstr long wstr long wstr long)
170 stdcall SQLTablePrivilegesW(long wstr long wstr long wstr long)
171 stdcall SQLDriversW(long long wstr long ptr ptr long ptr)
173 stdcall SQLSetDescFieldW(long long long ptr long)
176 stdcall SQLSetStmtAttrW(long long ptr long)
206 stdcall SQLColAttributesA(long long long ptr long ptr ptr) SQLColAttributes
207 stdcall SQLConnectA(long str long str long str long) SQLConnect
208 stdcall SQLDescribeColA(long long ptr long ptr ptr ptr ptr ptr) SQLDescribeCol
210 stdcall SQLErrorA(long long long ptr ptr ptr long ptr) SQLError
211 stdcall SQLExecDirectA(long str long) SQLExecDirect
217 stdcall SQLGetCursorNameA(long ptr long ptr) SQLGetCursorName
219 stdcall SQLPrepareA(long str long) SQLPrepare
221 stdcall SQLSetCursorNameA(long str long) SQLSetCursorName
227 stdcall SQLColAttributeA(long long long ptr long ptr ptr) SQLColAttribute
232 stdcall SQLGetConnectAttrA(long long ptr long ptr) SQLGetConnectAttr
233 stdcall SQLGetDescFieldA(long long long ptr long ptr) SQLGetDescField
234 stdcall SQLGetDescRecA(long long ptr long ptr ptr ptr ptr ptr ptr ptr) SQLGetDescRec
235 stdcall SQLGetDiagFieldA(long long long long ptr long ptr) SQLGetDiagField
236 stdcall SQLGetDiagRecA(long long long ptr ptr ptr long ptr) SQLGetDiagRec
238 stdcall SQLGetStmtAttrA(long long ptr long ptr) SQLGetStmtAttr
239 stdcall SQLSetConnectAttrA(long long ptr long) SQLSetConnectAttr
240 stdcall SQLColumnsA(long str long str long str long str long) SQLColumns
241 stdcall SQLDriverConnectA(long long str long ptr long ptr long) SQLDriverConnect
242 stdcall SQLGetConnectOptionA(long long ptr) SQLGetConnectOption
245 stdcall SQLGetInfoA(long long ptr long ptr) SQLGetInfo
247 stdcall SQLGetTypeInfoA(long long) SQLGetTypeInfo
250 stdcall SQLSetConnectOptionA(long long long) SQLSetConnectOption
252 stdcall SQLSpecialColumnsA(long long str long str long str long long long) SQLSpecialColumns
253 stdcall SQLStatisticsA(long str long str long str long long long) SQLStatistics
254 stdcall SQLTablesA(long str long str long str long str long) SQLTables
255 stdcall SQLBrowseConnectA(long str long ptr long ptr) SQLBrowseConnect
256 stdcall SQLColumnPrivilegesA(long str long str long str long str long) SQLColumnPrivileges
257 stdcall SQLDataSourcesA(long long str long ptr ptr long ptr) SQLDataSources
260 stdcall SQLForeignKeysA(long str long str long str long str long str long str long) SQLForeignKeys
262 stdcall SQLNativeSqlA(long str long ptr long ptr) SQLNativeSql
265 stdcall SQLPrimaryKeysA(long str long str long str long) SQLPrimaryKeys
266 stdcall SQLProcedureColumnsA(long str long str long str long str long) SQLProcedureColumns
267 stdcall SQLProceduresA(long str long str long str long) SQLProcedures
270 stdcall SQLTablePrivilegesA(long str long str long str long) SQLTablePrivileges
271 stdcall SQLDriversA(long long str long ptr ptr long ptr) SQLDrivers
273 stdcall SQLSetDescFieldA(long long long ptr long) SQLSetDescField
276 stdcall SQLSetStmtAttrA(long long ptr long) SQLSetStmtAttr
300 stub    ODBCSharedTraceFlag
301 stub    ODBCQualifyFileDSNW


 @ stub    LockHandle
 @ stub    ODBCInternalConnectW
 @ stub    OpenODBCPerfData
 @ stub    PostComponentError
 @ stub    PostODBCComponentError
 @ stub    PostODBCError
 @ stub    SearchStatusCode
 @ stub    VFreeErrors
 @ stub    VRetrieveDriverErrorsRowCol
 @ stub    ValidateErrorQueue
