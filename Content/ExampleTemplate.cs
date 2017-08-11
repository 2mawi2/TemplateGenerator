 public class ###Repository : SearchableRepository<###Entity, ###, ###.SortBy, ###.FilterAttribute>, I###Repository
    {
        private readonly Lazy<WaWiContext> _context;
        protected override DbContext Context => _context.Value;

        public ###Repository(Lazy<WaWiContext> context, IMapper mapper, ICurrentUser currentUser) : base(mapper, currentUser)
        {
            _context = context;
        }

        public async Task<IEnumerable<###>> GetByContactAsync(int contactId) =>
            await Find(i => i.Contact.ContactId.Equals(contactId));

        protected override SearchQuery<###Entity, ###, ###.SortBy, ###.FilterAttribute> CreateSearchQuery()
        {
            return new ###SearchQuery(Context, Mapper);
        }
    }