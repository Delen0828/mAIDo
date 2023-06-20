addstyle='''
*{
  color: #ffffff;

  font-family: Roboto;

  
    font-size: 13px;
  

  
    line-height: 13px;
  

  selection-background-color: #6effe8;
  selection-color: #000000;
}

*:focus {
   outline: none;
}

/*  ------------------------------------------------------------------------  */
/*  Custom colors  */

.danger{
  color: #dc3545;
  background-color: transparent;
}

.warning{
  color: #ffc107;
  background-color: transparent;
}

.success{
  color: #17a2b8;
  background-color: transparent;
}

.danger:disabled{
  color: rgba(220, 53, 69, 0.4);
  border-color: rgba(220, 53, 69, 0.4);
}

.warning:disabled{
  color: rgba(255, 193, 7, 0.4);
  border-color: rgba(255, 193, 7, 0.4);
}

.success:disabled{
  color: rgba(23, 162, 184, 0.4);
  border-color: rgba(23, 162, 184, 0.4);
}

.danger:flat:disabled{
  background-color: rgba(220, 53, 69, 0.1);
}

.warning:flat:disabled{
  background-color: rgba(255, 193, 7, 0.1);
}

.success:flat:disabled{
  background-color: rgba(23, 162, 184, 0.1);
}

/*  ------------------------------------------------------------------------  */
/*  Basic widgets  */

QWidget {
  background-color: #31363b;
}

QGroupBox,
QFrame {
  background-color: #31363b;
  border: 2px solid #4f5b62;
  border-radius: 4px;
}

QGroupBox.fill_background,
QFrame.fill_background {
  background-color: #232629;
  border: 2px solid #232629;
  border-radius: 4px;
}

QSplitter {
  background-color: transparent;
  border: none
}

QStatusBar {
  color: #ffffff;
  background-color: rgba(79, 91, 98, 0.2);
  border-radius: 0px;
}

QScrollArea,
QStackedWidget,
QWidget > QToolBox,
QToolBox > QWidget,
QTabWidget > QWidget {
  border: none;
}

QTabWidget::pane {
  border: none;
}

/*  ------------------------------------------------------------------------  */
/*  Inputs  */

QDateTimeEdit,
QSpinBox,
QDoubleSpinBox,
QTextEdit,
QLineEdit,
QPushButton {
  color: #1de9b6;
  background-color: #31363b;
  border: 2px solid #1de9b6;
  border-radius: 4px;
  height: 32px;
}

QDateTimeEdit,
QSpinBox,
QDoubleSpinBox,
QTreeView,
QListView,
QLineEdit,
QComboBox {
  padding-left: 16px;
  border-radius: 0px;
  background-color: #232629;
  border-width: 0 0 2px 0;
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  height: 32px;
}

QPlainTextEdit {
  border-radius: 4px;
  padding: 8px 16px;
  background-color: #31363b;
  border: 2px solid #4f5b62;
}

QTextEdit {
  padding: 8px 16px;
  border-radius: 4px;
  background-color: #232629;
}

QDateTimeEdit:disabled,
QSpinBox:disabled,
QDoubleSpinBox:disabled,
QTextEdit:disabled,
QLineEdit:disabled {
  color: rgba(29, 233, 182, 0.2);
  background-color: rgba(35, 38, 41, 0.75);
  border: 2px solid rgba(29, 233, 182, 0.2);
  border-width: 0 0 2px 0;
  padding: 0px 16px;
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  height: 32px;
}

/*  ------------------------------------------------------------------------  */
/*  QComboBox  */

QComboBox {
  color: #1de9b6;
  border: 1px solid #1de9b6;
  border-width: 0 0 2px 0;
  background-color: #232629;
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  height: 32px;
}

QComboBox:disabled {
  color: rgba(29, 233, 182, 0.2);
  background-color: rgba(35, 38, 41, 0.75);
  border-bottom: 2px solid rgba(29, 233, 182, 0.2);
}

QComboBox::drop-down {
  border: none;
  color: #1de9b6;
  width: 20px;
}

QComboBox::down-arrow {
  image: url(icon:/primary/downarrow.svg);
  margin-right: 12px;
}

QComboBox::down-arrow:disabled {
  image: url(icon:/disabled/downarrow.svg);
  margin-right: 12px;
}

QComboBox QAbstractItemView {
  background-color: #232629;
  border: 2px solid #4f5b62;
  border-radius: 4px;
}

QComboBox[frame='false'] {
  color: #1de9b6;
  background-color: transparent;
  border: 1px solid transparent;
}
QComboBox[frame='false']:disabled {
  color: rgba(29, 233, 182, 0.2);
}

/*  ------------------------------------------------------------------------  */
/*  Spin buttons  */

QDateTimeEdit::up-button,
QDoubleSpinBox::up-button,
QSpinBox::up-button {
  subcontrol-origin: border;
  subcontrol-position: top right;
  width: 20px;
  image: url(icon:/primary/uparrow.svg);
  border-width: 0px;
  margin-right: 5px;
}

QDateTimeEdit::up-button:disabled,
QDoubleSpinBox::up-button:disabled,
QSpinBox::up-button:disabled {
  image: url(icon:/disabled/uparrow.svg);
}

QDateTimeEdit::down-button,
QDoubleSpinBox::down-button,
QSpinBox::down-button {
  subcontrol-origin: border;
  subcontrol-position: bottom right;
  width: 20px;
  image: url(icon:/primary/downarrow.svg);
  border-width: 0px;
  border-top-width: 0;
  margin-right: 5px;
}

QDateTimeEdit::down-button:disabled,
QDoubleSpinBox::down-button:disabled,
QSpinBox::down-button:disabled {
  image: url(icon:/disabled/downarrow.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QPushButton  */

QPushButton {
  text-transform: uppercase;
  margin: 0px;
  padding: 1px 16px;
  height: 32px;
  font-weight: bold;

  
    border-radius: 4px;
  


}

QPushButton:checked,
QPushButton:pressed {
  color: #31363b;
  background-color: #1de9b6;
}

QPushButton:flat {
  margin: 0px;
  color: #1de9b6;
  border: none;
  background-color: transparent;
}

QPushButton:flat:hover {
  background-color: rgba(29, 233, 182, 0.2);
}

QPushButton:flat:pressed,
QPushButton:flat:checked {
  background-color: rgba(29, 233, 182, 0.1);
}

QPushButton:disabled {
  color: rgba(79, 91, 98, 0.75);
  background-color: transparent;
  border-color:  #4f5b62;
}

QPushButton:flat:disabled {
  color: rgba(79, 91, 98, 0.75);
  background-color: rgba(79, 91, 98, 0.25);
  border: none;
}

QPushButton:disabled {
  border: 2px solid rgba(79, 91, 98, 0.75);
}

QPushButton:checked:disabled {
  color: #232629;
  background-color: #4f5b62;
  border-color:  #4f5b62;
}

/*  ------------------------------------------------------------------------  */
/*  QTabBar  */

QTabBar{
  text-transform: uppercase;
  font-weight: bold;
}

QTabBar::tab {
  color: #ffffff;
  border: 0px;
}

QTabBar::tab:bottom,
QTabBar::tab:top{
  padding: 0 16px;
  height: 28px;
}

QTabBar::tab:left,
QTabBar::tab:right{
  padding: 16px 0;
  width: 28px;
}

QTabBar::tab:top:selected,
QTabBar::tab:top:hover {
  color: #1de9b6;
  border-bottom: 2px solid #1de9b6;
}

QTabBar::tab:bottom:selected,
QTabBar::tab:bottom:hover {
  color: #1de9b6;
  border-top: 2px solid #1de9b6;
}

QTabBar::tab:right:selected,
QTabBar::tab:right:hover {
  color: #1de9b6;
  border-left: 2px solid #1de9b6;
}

QTabBar::tab:left:selected,
QTabBar::tab:left:hover {
  color: #1de9b6;
  border-right: 2px solid #1de9b6;
}

QTabBar QToolButton:hover,
QTabBar QToolButton {
  border: 20px;
  background-color: #31363b;
}

QTabBar QToolButton::up-arrow {
  image: url(icon:/disabled/uparrow2.svg);
}

QTabBar QToolButton::up-arrow:hover {
  image: url(icon:/primary/uparrow2.svg);
}

QTabBar QToolButton::down-arrow {
  image: url(icon:/disabled/downarrow2.svg);
}

QTabBar QToolButton::down-arrow:hover {
  image: url(icon:/primary/downarrow2.svg);
}

QTabBar QToolButton::right-arrow {
  image: url(icon:/primary/rightarrow2.svg);
}

QTabBar QToolButton::right-arrow:hover {
  image: url(icon:/disabled/rightarrow2.svg);
}

QTabBar QToolButton::left-arrow {
  image: url(icon:/primary/leftarrow2.svg);
}

QTabBar QToolButton::left-arrow:hover {
  image: url(icon:/disabled/leftarrow2.svg);
}

QTabBar::close-button {
  image: url(icon:/disabled/tab_close.svg);
}

QTabBar::close-button:hover {
  image: url(icon:/primary/tab_close.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QGroupBox  */

QGroupBox {
  padding: 16px;
  padding-top: 36px;
  line-height: ;
  text-transform: uppercase;
  font-size: ;
}

QGroupBox::title {
  color: rgba(255, 255, 255, 0.4);
  subcontrol-origin: margin;
  subcontrol-position: top left;
  padding: 16px;
  background-color: #31363b;
  background-color: transparent;
  height: 36px;
}

/*  ------------------------------------------------------------------------  */
/*  QRadioButton and QCheckBox labels  */

QRadioButton,
QCheckBox {
  spacing: 12px;
  color: #ffffff;
  line-height: 14px;
  height: 36px;
  background-color: transparent;
  spacing: 5px;
}

QRadioButton:disabled,
QCheckBox:disabled {
  color: rgba(255, 255, 255, 0.3);
}

/*  ------------------------------------------------------------------------  */
/*  General Indicators  */

QGroupBox::indicator {
  width: 24px;
  height: 24px;
  border-radius: 3px;
}

QMenu::indicator,
QListView::indicator,
QTableWidget::indicator,
QRadioButton::indicator,
QCheckBox::indicator {
  width: 28px;
  height: 28px;
  border-radius: 4px;
 }

/*  ------------------------------------------------------------------------  */
/*  QListView Indicator  */

QListView::indicator:checked,
QListView::indicator:checked:selected,
QListView::indicator:checked:focus {
  image: url(icon:/primary/checklist.svg);
}

QListView::indicator:checked:selected:active {
  image: url(icon:/primary/checklist_invert.svg);
}

QListView::indicator:checked:disabled {
  image: url(icon:/disabled/checklist.svg);
}

QListView::indicator:indeterminate,
QListView::indicator:indeterminate:selected,
QListView::indicator:indeterminate:focus {
  image: url(icon:/primary/checklist_indeterminate.svg);
}

QListView::indicator:indeterminate:selected:active {
  image: url(icon:/primary/checklist_indeterminate_invert.svg);
}

QListView::indicator:indeterminate:disabled {
  image: url(icon:/disabled/checklist_indeterminate.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QTableView Indicator  */

QTableView::indicator:enabled:checked,
QTableView::indicator:enabled:checked:selected,
QTableView::indicator:enabled:checked:focus {
  image: url(icon:/primary/checkbox_checked.svg);
}

QTableView::indicator:checked:selected:active {
  image: url(icon:/primary/checkbox_checked_invert.svg);
}

QTableView::indicator:disabled:checked,
QTableView::indicator:disabled:checked:selected,
QTableView::indicator:disabled:checked:focus {
  image: url(icon:/disabled/checkbox_checked.svg);
}

QTableView::indicator:enabled:unchecked,
QTableView::indicator:enabled:unchecked:selected,
QTableView::indicator:enabled:unchecked:focus {
  image: url(icon:/primary/checkbox_unchecked.svg);
}

QTableView::indicator:unchecked:selected:active {
  image: url(icon:/primary/checkbox_unchecked_invert.svg);
}

QTableView::indicator:disabled:unchecked,
QTableView::indicator:disabled:unchecked:selected,
QTableView::indicator:disabled:unchecked:focus {
  image: url(icon:/disabled/checkbox_unchecked.svg);
}

QTableView::indicator:enabled:indeterminate,
QTableView::indicator:enabled:indeterminate:selected,
QTableView::indicator:enabled:indeterminate:focus {
  image: url(icon:/primary/checkbox_indeterminate.svg);
}

QTableView::indicator:indeterminate:selected:active {
  image: url(icon:/primary/checkbox_indeterminate_invert.svg);
}

QTableView::indicator:disabled:indeterminate,
QTableView::indicator:disabled:indeterminate:selected,
QTableView::indicator:disabled:indeterminate:focus {
  image: url(icon:/disabled/checkbox_indeterminate.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QCheckBox and QGroupBox Indicator  */

QCheckBox::indicator:checked,
QGroupBox::indicator:checked {
  image: url(icon:/primary/checkbox_checked.svg);
}

QCheckBox::indicator:unchecked,
QGroupBox::indicator:unchecked {
  image: url(icon:/primary/checkbox_unchecked.svg);
}

QCheckBox::indicator:indeterminate,
QGroupBox::indicator:indeterminate {
  image: url(icon:/primary/checkbox_indeterminate.svg);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled {
  image: url(icon:/disabled/checkbox_checked.svg);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled {
  image: url(icon:/disabled/checkbox_unchecked.svg);
}

QCheckBox::indicator:indeterminate:disabled,
QGroupBox::indicator:indeterminate:disabled {
  image: url(icon:/disabled/checkbox_indeterminate.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QRadioButton Indicator  */

QRadioButton::indicator:checked {
  image: url(icon:/primary/radiobutton_checked.svg);
}

QRadioButton::indicator:unchecked {
  image: url(icon:/primary/radiobutton_unchecked.svg);
}

QRadioButton::indicator:checked:disabled {
  image: url(icon:/disabled/radiobutton_checked.svg);
}

QRadioButton::indicator:unchecked:disabled {
  image: url(icon:/disabled/radiobutton_unchecked.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QDockWidget  */

QDockWidget {
  color: #ffffff;
  text-transform: uppercase;
  border: 2px solid #232629;
  titlebar-close-icon: url(icon:/primary/close.svg);
  titlebar-normal-icon: url(icon:/primary/float.svg);
  border-radius: 4px;
}

QDockWidget::title {
  text-align: left;
  padding-left: 36px;
  padding: 3px;
  margin-top: 4px;
}

/*  ------------------------------------------------------------------------  */
/*  QComboBox indicator  */

QComboBox::indicator:checked {
  image: url(icon:/primary/checklist.svg);
}

QComboBox::indicator:checked:selected {
  image: url(icon:/primary/checklist_invert.svg);
}

/*  ------------------------------------------------------------------------  */
/*  Menu Items  */

QComboBox::item,
QCalendarWidget QMenu::item,
QMenu::item {
  
    height: 28px;
  
  border: 8px solid transparent;
  color: #ffffff;
}

QCalendarWidget QMenu::item,
QMenu::item {
  
    
      padding: 0px 24px 0px 8px;  /* pyqt5 */
    
  
}


QComboBox::item:selected,
QCalendarWidget QMenu::item:selected,
QMenu::item:selected {
  color: #000000;
  background-color: #6effe8;
  border-radius: 0px;
}

QComboBox::item:disabled,
QCalendarWidget QMenu::item:disabled,
QMenu::item:disabled {
  color: rgba(255, 255, 255, 0.3);
}

/*  ------------------------------------------------------------------------  */
/*  QMenu  */

QCalendarWidget QMenu,
QMenu {
  background-color: #232629;
  border: 2px solid #4f5b62;
  border-radius: 4px;
}

QMenu::separator {
  height: 2px;
  background-color: #4f5b62;
  margin-left: 2px;
  margin-right: 2px;
}

QMenu::right-arrow{
  image: url(icon:/primary/rightarrow.svg);
  width: 16px;
  height: 16px;
}

QMenu::right-arrow:selected{
  image: url(icon:/disabled/rightarrow.svg);
}

QMenu::indicator:non-exclusive:unchecked {
  image: url(icon:/primary/checkbox_unchecked.svg);
}

QMenu::indicator:non-exclusive:unchecked:selected {
  image: url(icon:/primary/checkbox_unchecked_invert.svg);
}

QMenu::indicator:non-exclusive:checked {
  image: url(icon:/primary/checkbox_checked.svg);
}

QMenu::indicator:non-exclusive:checked:selected {
  image: url(icon:/primary/checkbox_checked_invert.svg);
}

QMenu::indicator:exclusive:unchecked {
  image: url(icon:/primary/radiobutton_unchecked.svg);
}

QMenu::indicator:exclusive:unchecked:selected {
  image: url(icon:/primary/radiobutton_unchecked_invert.svg);
}

QMenu::indicator:exclusive:checked {
  image: url(icon:/primary/radiobutton_checked.svg);
}

QMenu::indicator:exclusive:checked:selected {
  image: url(icon:/primary/radiobutton_checked_invert.svg);
}

/*  ------------------------------------------------------------------------  */
/*  QMenuBar  */

QMenuBar {
  background-color: #232629;
  color: #ffffff;
}

QMenuBar::item {
  height: 32px;
  padding: 8px;
  background-color: transparent;
  color: #ffffff;
}

QMenuBar::item:selected,
QMenuBar::item:pressed {
  color: #000000;
  background-color: #6effe8;
}

/*  ------------------------------------------------------------------------  */
/*  QToolBox  */

QToolBox::tab {
  background-color: #232629;
  color: #ffffff;
  text-transform: uppercase;
  border-radius: 4px;
  padding-left: 15px;
}

QToolBox::tab:selected,
QToolBox::tab:hover {
  background-color: rgba(29, 233, 182, 0.2);
}

/*  ------------------------------------------------------------------------  */
/*  QProgressBar  */

QProgressBar {
  border-radius: 0;
  background-color: #4f5b62;
  text-align: center;
  color: transparent;
}

QProgressBar::chunk {
  background-color: #1de9b6;
}

/*  ------------------------------------------------------------------------  */
/*  QScrollBar  */

QScrollBar:horizontal {
  border: 0;
  background: #232629;
  height: 8px;
}

QScrollBar:vertical {
  border: 0;
  background: #232629;
  width: 8px;
}

QScrollBar::handle {
  background: rgba(29, 233, 182, 0.1);
}

QScrollBar::handle:horizontal {
  min-width: 24px;
}

QScrollBar::handle:vertical {
  min-height: 24px;
}

QScrollBar::handle:vertical:hover,
QScrollBar::handle:horizontal:hover {
  background: #1de9b6;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
  border: 0;
  background: transparent;
  width: 0px;
  height: 0px;
}

/*  ------------------------------------------------------------------------  */
/*  QScrollBar-Big  */

QScrollBar.big:horizontal {
  border: 0;
  background: #232629;
  height: 36px;
}

QScrollBar.big:vertical {
  border: 0;
  background: #232629;
  width: 36px;
}

QScrollBar.big::handle,
QScrollBar.big::handle:vertical:hover,
QScrollBar.big::handle:horizontal:hover {
  background: #1de9b6;
}

QScrollBar.big::handle:horizontal {
  min-width: 24px;
}

QScrollBar.big::handle:vertical {
  min-height: 24px;
}

QScrollBar.big::add-line:vertical,
QScrollBar.big::sub-line:vertical,
QScrollBar.big::add-line:horizontal,
QScrollBar.big::sub-line:horizontal {
  border: 0;
  background: transparent;
  width: 0px;
  height: 0px;
}

/*  ------------------------------------------------------------------------  */
/*  QSlider  */

QSlider:horizontal {
  min-height: 24px;
  max-height: 24px;
}

QSlider:vertical {
  min-width: 24px;
  max-width: 24px;
}

QSlider::groove:horizontal {
  height: 4px;
  background: #393939;
  margin: 0 12px;
}

QSlider::groove:vertical {
  width: 4px;
  background: #393939;
  margin: 12px 0;
  border-radius: 24px;
}

QSlider::handle:horizontal {
  image: url(icon:/primary/slider.svg);
  width: 24px;
  height: 24px;
  margin: -24px -12px;
}

QSlider::handle:vertical {
  image: url(icon:/primary/slider.svg);
  border-radius: 24px;
  width: 24px;
  height: 24px;
  margin: -12px -24px;
}

QSlider::add-page {
background: #232629;
}

QSlider::sub-page {
background: #1de9b6;
}

/*  ------------------------------------------------------------------------  */
/*  QLabel  */

QLabel {
  border: none;
  background: transparent;
  color: #ffffff
}

QLabel:disabled {
  color: rgba(255, 255, 255, 0.2)
}

/*  ------------------------------------------------------------------------  */
/*  VLines and HLinex  */

QFrame[frameShape="4"] {
    border-width: 1px 0 0 0;
    background: none;
}

QFrame[frameShape="5"] {
    border-width: 0 1px 0 0;
    background: none;
}

QFrame[frameShape="4"],
QFrame[frameShape="5"] {
  border-color: #4f5b62;
}

/*  ------------------------------------------------------------------------  */
/*  QToolBar  */

QToolBar {
  background: #31363b;
  border: 0px solid;
}

QToolBar:horizontal {
  border-bottom: 1px solid #4f5b62;
}

QToolBar:vertical {
  border-right: 1px solid #4f5b62;
}

QToolBar::handle:horizontal {
  image: url(icon:/primary/toolbar-handle-horizontal.svg);
}

QToolBar::handle:vertical {
  image: url(icon:/primary/toolbar-handle-vertical.svg);
}

QToolBar::separator:horizontal {
  border-right: 1px solid #4f5b62;
  border-left: 1px solid #4f5b62;
  width: 1px;
}

QToolBar::separator:vertical {
  border-top: 1px solid #4f5b62;
  border-bottom: 1px solid #4f5b62;
  height: 1px;
}


/*  ------------------------------------------------------------------------  */
/*  QToolButton  */

QToolButton {
  background: #31363b;
  border: 0px;
  height: 36px;
  margin: 3px;
  padding: 3px;
  border-right: 12px solid #31363b;
  border-left: 12px solid #31363b;
}

QToolButton:hover {
  background: #4f5b62;
  border-right: 12px solid #4f5b62;
  border-left: 12px solid #4f5b62;
}

QToolButton:pressed {
  background: #232629;
  border-right: 12px solid #232629;
  border-left: 12px solid #232629;
}

QToolButton:checked {
  background: #4f5b62;
  border-left: 12px solid #4f5b62;
  border-right: 12px solid #1de9b6;
}

/*  ------------------------------------------------------------------------  */
/*  General viewers  */

QTableView {
  background-color: #31363b;
  border: 1px solid #232629;
  border-radius: 4px;
}

QTreeView,
QListView {
  border-radius: 4px;
  padding: 4px;
  margin: 0px;
  border: 0px;
}

QTableView::item,
QTreeView::item,
QListView::item {
  padding: 4px;
  min-height: 32px;
  color: #ffffff;
  selection-color: #ffffff; /* For Windows */
}

/*  ------------------------------------------------------------------------  */
/*  Items Selection */

QTableView::item:selected,
QTreeView::item:selected,
QListView::item:selected {
  background-color: rgba(29, 233, 182, 0.2);
  selection-background-color: rgba(29, 233, 182, 0.2);
  color: #ffffff;
  selection-color: #ffffff; /* For Windows */
}

QTableView::item:selected:focus,
QTreeView::item:selected:focus,
QListView::item:selected:focus {
  background-color: #1de9b6;
  selection-background-color: #1de9b6;
  color: #000000;
  selection-color: #000000; /* For Windows */
}

QTableView {
  selection-background-color: rgba(29, 233, 182, 0.2);
}

QTableView:focus {
  selection-background-color: #1de9b6;
}

QTableView::item:disabled {
  color: rgba(255, 255, 255, 0.3);
  selection-color: rgba(255, 255, 255, 0.3);
  background-color: #232629;
  selection-background-color: #232629;
}

/*  ------------------------------------------------------------------------  */
/*  QTreeView  */

QTreeView::branch{
  background-color: #232629;
}

QTreeView::branch:closed:has-children:has-siblings,
QTreeView::branch:closed:has-children:!has-siblings {
  image: url(icon:/primary/branch-closed.svg);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
  image: url(icon:/primary/branch-open.svg);
}

QTreeView::branch:has-siblings:!adjoins-item {
  border-image: url(icon:/disabled/vline.svg) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(icon:/disabled/branch-more.svg) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item,
QTreeView::branch:has-children:!has-siblings:adjoins-item {
    border-image: url(icon:/disabled/branch-end.svg) 0;
}

QTreeView QHeaderView::section {
  border: none;
}


/*  ------------------------------------------------------------------------  */
/*  Custom buttons  */

QPushButton.danger {
  border-color: #dc3545;
  color: #dc3545;
}

QPushButton.danger:checked,
QPushButton.danger:pressed {
  color: #31363b;
  background-color: #dc3545;
}

QPushButton.warning{
  border-color: #ffc107;
  color: #ffc107;
}

QPushButton.warning:checked,
QPushButton.warning:pressed {
  color: #31363b;
  background-color: #ffc107;
}

QPushButton.success {
  border-color: #17a2b8;
  color: #17a2b8;
}

QPushButton.success:checked,
QPushButton.success:pressed {
  color: #31363b;
  background-color: #17a2b8;
}

QPushButton.danger:flat:hover {
  background-color: rgba(220, 53, 69, 0.2);
}

QPushButton.danger:flat:pressed,
QPushButton.danger:flat:checked {
  background-color: rgba(220, 53, 69, 0.1);
  color: #dc3545;
}

QPushButton.warning:flat:hover {
  background-color: rgba(255, 193, 7, 0.2);
}

QPushButton.warning:flat:pressed,
QPushButton.warning:flat:checked {
  background-color: rgba(255, 193, 7, 0.1);
  color: #ffc107;
}

QPushButton.success:flat:hover {
  background-color: rgba(23, 162, 184, 0.2);
}

QPushButton.success:flat:pressed,
QPushButton.success:flat:checked {
  background-color: rgba(23, 162, 184, 0.1);
  color: #17a2b8;
}

/*  ------------------------------------------------------------------------  */
/*  QTableView  */

QTableCornerButton::section {
  background-color: #232629;
  border-radius: 0px;
  border-right: 1px solid;
  border-bottom: 1px solid;
  border-color: #31363b;
}

QTableView {
  alternate-background-color: rgba(35, 38, 41, 0.7);
}

QHeaderView {
  border: none;
}

QHeaderView::section {
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  background-color: #232629;
  padding: 0 24px;
  height: 36px;
  border-radius: 0px;
  border-right: 1px solid;
  border-bottom: 1px solid;
  border-color: #31363b;
}

QHeaderView::section:vertical {

}

QHeaderView::section:horizontal {

}

/*  ------------------------------------------------------------------------  */
/*  QLCDNumber  */

QLCDNumber {
  color: #1de9b6;
  background-color:rgba(29, 233, 182, 0.1);
  border: 1px solid rgba(29, 233, 182, 0.3);
  border-radius: 4px;
}

/*  ------------------------------------------------------------------------  */
/*  QCalendarWidget  */

#qt_calendar_prevmonth {
  qproperty-icon: url(icon:/primary/leftarrow.svg);
}

#qt_calendar_nextmonth {
  qproperty-icon: url(icon:/primary/rightarrow.svg);
}

/*  ------------------------------------------------------------------------  */
/*  Inline QLineEdit  */

QTreeView QLineEdit,
QTableView QLineEdit,
QListView QLineEdit {
  color: #ffffff;
  background-color: #232629;
  border: 1px solid unset;
  border-radius: unset;
  padding: unset;
  padding-left: unset;
  height: unset;
  border-width: unset;
  border-top-left-radius: unset;
  border-top-right-radius: unset;
}

/*  ------------------------------------------------------------------------  */
/*  QToolTip  */

QToolTip {
  padding: 4px;
  border: 1px solid #31363b;
  border-radius: 4px;
  color: #ffffff;
  background-color: #4f5b62;
}

/*  ------------------------------------------------------------------------  */
/*  QDialog  */



QDialog QToolButton:disabled {
  background-color: #232629;
  color: #ffffff
}

/*  ------------------------------------------------------------------------  */
/*  Grips  */


QMainWindow::separator:vertical,
QSplitter::handle:horizontal {
  image: url(icon:/primary/splitter-horizontal.svg);
}

QMainWindow::separator:horizontal,
QSplitter::handle:vertical {
  image: url(icon:/primary/splitter-vertical.svg);
}

QSizeGrip {
  image: url(icon:/primary/sizegrip.svg);
  background-color: transparent;
}

QMenuBar QToolButton:hover,
QMenuBar QToolButton:pressed,
QMenuBar QToolButton {
  border-width: 0;
  border-left: 10px;
  border-image: url(icon:/primary/rightarrow2.svg);
  background-color: transparent;
}
'''