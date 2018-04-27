""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nocompatible              " be iMproved, required
filetype off                  " required


" Keep Plugin commands between vundle#begin/end.
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/nerdtree'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'tpope/vim-fugitive'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'tpope/vim-commentary'
Plugin 'godlygeek/tabular'
Plugin 'thinca/vim-quickrun'
Plugin 'junegunn/fzf'
Plugin 'itchyny/lightline.vim'
Plugin 'easymotion/vim-easymotion'
call vundle#end()            " required
filetype plugin indent on    " required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"All modes mappings
map <C-o> :NERDTreeToggle<CR>
map <Leader> <Plug>(easymotion-prefix)
"Insert mode mappings
imap øø <Esc>


"Normal mode mappings
nmap , <Leader>

colorscheme desert
syntax on
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Sets
set autoindent
set tabstop=4
set number
set shiftwidth=4
set expandtab
set wildmode=longest,list,full
set wildmenu
set laststatus=2
set noshowmode
set guifont=Monaco:h14
"Lets
let g:indent_guides_enable_on_vim_startup = 1
