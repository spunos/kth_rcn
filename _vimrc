source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin

set nocompatible
set nobackup
set noswapfile
set history=50		" keep 50 lines of command line history
set incsearch		" do incremental searching
set number          " show line numbers
set tabstop=4       " a hard tab displays as 4 columns
set softtabstop=4   " insert/delete 4 spaces when hitting a tab/backspace
set shiftround      " round indent to multiple of 'shiftwidth'
set shiftwidth=4    " operation >> indents 4 columns; << unindents 4 columns
set textwidth=79    " lines longer than 79 columns will be broken
set columns=90
set lines=40
set smarttab
set expandtab       " inserts spaces when hitting tabs
set autoindent      " align the new line indent with the previous line
set clipboard=unnamed   "copies to the clipboard
set vb                    " No beeping.
set wildmenu                      " Enhanced command line completion.
set wildmode=list:longest         " Complete files like a shell.
set encoding=utf-8  " allows for åäö among others

syntax on
filetype indent on
filetype on
filetype plugin on

" Toggle line numbers and fold column for easy copying:
nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>

" Execute file being edited with F5:
nnoremap <F5> :w<CR>:!python % <CR>

" Use <F7> and <F8> to switch between tabs:
nnoremap <F7> :tabp<CR>
nnoremap <F8> :tabn<CR>

" Use <F9> and <F10> to switch between files in the buffer:
nnoremap <F9> :bp<CR>
nnoremap <F10> :bn<CR>

set t_Co=256
:colo zenburn

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction
