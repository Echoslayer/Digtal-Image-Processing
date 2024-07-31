/*像素類別宣告*/
class TMyPoint
{
  public:
    int X;
    int Y;
  bool Used;
};

/*主要視窗宣告*/
class TMainForm : public TForm
{
  private:
    AnsiString  MyFileName;
  public:

  /*記錄鄰居的陣列*/
  int m_intNeighbor[9];
  /* | p0 p1 p2 |*/
  /* | p3 p4 p5 |*/
  /* | p6 p7 p8 |*/

  TMyPoint points[2304];
  TRect bmpRect;
  public:
    __fastcall TMainForm(TComponent* Owner);
    void __fastcall GetNeighbor(int x, int y);
    bool __fastcall Condition_a(void);
    bool __fastcall Condition_b(void);
    bool __fastcall pointsMultiply(int a, int b, int c);
    bool __fastcall BasicStep1(int x, int y);
    bool __fastcall BasicStep2(int x, int y);
    
  // The Following Functions are Management of Deleted Points
    void __fastcall AddEntry(int x, int y);
    void __fastcall ClearEntry(void);
    void __fastcall DelEntry(void);
    bool __fastcall IsDelete(int x, int y);
    bool __fastcall IsEmpty();
    bool __fastcall ThinningPass1(TRect region);
    bool __fastcall ThinningPass2(TRect region);
};

/*取得鄰居資訊*/
/*輸入影像座標值x，y*/
void __fastcall TMainForm::GetNeighbor(int x, int y)
{
  x--; y--;
  for (int j=y; j<y+3; j++)
    for (int i=x; i<x+3; i++)
      m_intNeighbor[(i-x)+3*(j-y)]= MainForm->Canvas->Pixels[i][j]==clBlack)?1:0;
}

/*條件判斷式a*./
bool __fastcall TMainForm::Condition_a(void)
{
  int Function_P=0;
  for (int i=0; i<9; i++)
    if (i!=4) Function_P = Function_P + m_intNeighbor[i];
  if (Function_P<=6 && Function_P>=2) return TRUE;
  return FALSE;
}

/*條件判斷式b*/
bool __fastcall TMainForm::Condition_b(void)
{
  int Function_S=0;
  if (m_intNeighbor[0]==0 && m_intNeighbor[1]==1)
    Function_S++;
  if (m_intNeighbor[1]==0 && m_intNeighbor[2]==1)
    Function_S++;
  if (m_intNeighbor[2]==0 && m_intNeighbor[5]==1)
    Function_S++;
  if (m_intNeighbor[5]==0 && m_intNeighbor[8]==1)
    Function_S++;
  if (m_intNeighbor[8]==0 && m_intNeighbor[7]==1)
    Function_S++;
  if (m_intNeighbor[7]==0 && m_intNeighbor[6]==1)
    Function_S++;
  if (m_intNeighbor[6]==0 && m_intNeighbor[3]==1)
    Function_S++;
  if (m_intNeighbor[3]==0 && m_intNeighbor[0]==1)
    Function_S++;
  if (Function_S==1) return TRUE;
  return FALSE;
}

bool __fastcall TMainForm::pointsMultiply(int a, int b, int c)
{
  if (a*b*c == 0) return TRUE;
  return FALSE;
}

/*細化處理函式1*/
/*輸入影像座標x，y*/
bool __fastcall TMainForm::BasicStep1(int x, int y)
{
  BOOL Condition_c1, Condition_d1;
  GetNeighbor(x, y);
  Condition_c1 = pointsMultiply(m_intNeighbor[1],
  m_intNeighbor[5],
  m_intNeighbor[7]);
  Condition_d1 = pointsMultiply(m_intNeighbor[5],
  m_intNeighbor[7],
  m_intNeighbor[3]);
  if ( Condition_a() &&
       Condition_b() &&
       Condition_c1  &&
       Condition_d1 ) return TRUE;
  return FALSE;
}

/*細化處理函式2*/
/*輸入影像座標x，y*/
bool __fastcall TMainForm::BasicStep2(int x, int y)
{
  BOOL Condition_c2, Condition_d2; 
  GetNeighbor(x, y);
  Condition_c2 = pointsMultiply(m_intNeighbor[1],
  m_intNeighbor[5],
  m_intNeighbor[3]);
  Condition_d2 = pointsMultiply(m_intNeighbor[1],
  m_intNeighbor[7],
  m_intNeighbor[3]);
  if ( Condition_a() &&
       Condition_b() &&
       Condition_c2  &&
       Condition_d2 ) return TRUE;
  return FALSE;
}

void __fastcall TMainForm::AddEntry(int x, int y)
{
  for (int i=0; i<2043; i++)
  {
    if (points[i].Used == FALSE)
    {
      points[i].X = x; points[i].Y = y; points[i].Used = TRUE;
      break;
    }
  }
}

/*初始變數*/
void __fastcall TMainForm::DelEntry()
{
  for (int i=0; i<2043; i++)
  {
    if (points[i].Used == TRUE)
    {
       MainForm->Canvas->Pixels[points[i].X][points[i].Y] = clWhite;
       points[i].Used = FALSE;
    }
  }
}

bool __fastcall TMainForm::IsDelete(int x, int y)
{
  for (int i=0; i<2043; i++)
  {
    if ((points[i].X == x)&&(points[i].Y == y)) return TRUE;
  }
  return FALSE;
}

bool __fastcall TMainForm::IsEmpty()
{
  for (int i=0; i<2043; i++)
  {
    if (points[i].Used==TRUE) return FALSE;
  }
  return TRUE;
}

/*初始變數*/
void __fastcall TMainForm::ClearEntry()
{
  for (int i=0; i<2043; i++)
    points[i].Used = FALSE;
}

/*細化Pass1*/
/*輸入參數：一個矩形區域*/
bool __fastcall TMainForm::ThinningPass1(TRect region)
{
  for(int j=region.Left; j<=region.Right; j++)
  {
    for (int i=region.Top; i<=region.Bottom; i++)
      if (MainForm->Canvas->Pixels[i][j]==clBlack)
        if (BasicStep1(i, j))
          AddEntry(i, j);
  }  
  if (IsEmpty()) return FALSE;
  DelEntry();
  return TRUE;
}

/*細化Pass2*/
/*輸入參數：一個矩形區域*/
bool __fastcall TMainForm::ThinningPass2(TRect region)
{
  for(int j=region.Left; j<=region.Right; j++)
  {
    for (int i=region.Top; i<=region.Bottom; i++)
      if (MainForm->Canvas->Pixels[i][j]==clBlack)
        if (BasicStep2(i, j))   
          AddEntry(i, j);
  }
  if (IsEmpty()) return FALSE;
  DelEntry();
  return TRUE;
}

__fastcall TMainForm::TMainForm(TComponent* Owner)
	: TForm(Owner)
{
ClearEntry();
}

/*讀圖檔*/
void __fastcall TMainForm::Button1Click(TObject *Sender)
{
  MainForm->FormStyle = fsNormal;
  if (OpenDialog1->Execute())
  {
    MainForm->FormStyle = fsStayOnTop;
    MyFileName = OpenDialog1->FileName;
					    Graphics::TBitmap* MyBmp;
    MyBmp = new Graphics::TBitmap();
    MyBmp->LoadFromFile(MyFileName);
    MainForm->Canvas->Draw(0 ,0, MyBmp);
    bmpRect.Top = 0;
    bmpRect.Left = 0;
    bmpRect.Bottom = MyBmp->Height;
    bmpRect.Right = MyBmp->Width;
    delete MyBmp;
  }
}

/*開始做細化*/
void __fastcall TMainForm::Button2Click(TObject *Sender)
{
  Button2->Enabled = FALSE;
  bool Pass1=TRUE,Pass2=TRUE;
  while (Pass1 || Pass2)
  {
    Pass1 = ThinningPass1(bmpRect);
    Pass2 = ThinningPass2(bmpRect);
  }
  Button2->Enabled = TRUE;
}