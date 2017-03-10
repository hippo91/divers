" Nice colors
colorscheme desert

" Sourcing of syncolor.vim for every new buffer
autocmd BufRead,BufNewFile * source ~/.vim/after/syntax/syncolor.vim

" Enable syntax highlighting
syntax enable 

" Save session
nnoremap <leader>s :mksession<CR>

" Turn off search highlight
nnoremap <leader><space> :nohlsearch<CR> 

" Use spaces instead of tabs
set expandtab 

" Number of visual spaces per tab
set tabstop=2 
set shiftwidth=2

" Sets how many lines of history VIM has to remember
set history=700 

" Height of the command bar
set cmdheight=2 

" Print line numbers 
set number 

" Print the last command in bottom bar
set showcmd 

" Automatic indentation
set autoindent 
set cindent

if has("autocmd")
  " Load filetype-specific indent files
  filetype plugin indent on 
endif

" Visual autocomplete for command menu
set wildmenu 

" Ignore compiled files
set wildignore=*.o,*~,*.pyc 

" Show matching brackets when text indicator is over them
set showmatch 

" How many tenths of a second to blink when matching brackets
set mat=2 

" Minimal width of the line numbers margin
set numberwidth=3

" No linebreak
set tw=0

" Prefix of the lines created by a CR
set showbreak="|_>"

" No annoying sound on errors
set noerrorbells
set novisualbell

" Smart backspaces 
set backspace=indent,eol,start 

" Mouse support
set mouse=a 

" For regular expressions turn magic on
set magic 

" Always print tab line 
set showtabline=2 

" Set extra options when running in GUI mode
if has("gui_running")
    set guioptions-=T
    set t_Co=256
    set guitablabel=%n\ %f\ %l\ %m" Print tab number and relative path to the edited file
endif

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8 

" Use Unix as the standard file type
set ffs=unix,dos,mac 

" Automatic reload of a modified file
set autoread 

au CursorHold * checktime

" Search as characters are entered
set incsearch           

" Highlight matches
set hlsearch            

" Ignore case when searching
set ignorecase 

" When searching try to be smart about cases 
set smartcase 

" Enable folding
set foldenable 

" Open most folds by default (0 for none - 99 for all)
set foldlevelstart=10 

" 10 nested fold max
set foldnestmax=10 

" Space open/closes folds
nnoremap <space> za 

" Fold based on syntax
set foldmethod=syntax 

filetype plugin on
set omnifunc=syntaxcomplete#Complete

" Visual mode pressing * or # searches for the current selection
" Super useful! From an idea by Michael Naumann
vnoremap <silent> * :call VisualSelection('f')<CR>
vnoremap <silent> # :call VisualSelection('b')<CR>

" Switch CWD to the directory of the open buffer
map <leader>cd :cd %:p:h<cr>:pwd<cr>

" Always show the status line
set laststatus=2
set statusline=Path:\ %F\ \|\ Ligne:\ %l\ \|\ Colonne:\ %c\ \|\ Byte:\ %b-->0x%B

" Printing command
set printdevice=cp

" Editing pdf
:command! -complete=file -nargs=1 Rpdf :r !pdftotext -nopgbrk <q-args> - |fmt -csw78
